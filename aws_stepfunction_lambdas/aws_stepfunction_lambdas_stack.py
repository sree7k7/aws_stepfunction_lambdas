from aws_cdk import (
    # Duration,
    # core,
    Stack,
    Duration
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks


class AwsStepfunctionLambdasStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a step function
        # state machine definition
        # add below lambda functions with choice to the state machine

    # hello world lambda
        hello_world_lambda = _lambda.Function(
            self,
            "HelloWorldHandler",
            function_name="hello_world",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("lambda"),
            handler="helloworld.lambda_handler"
        )
        # Define the state machine
        # create a lambda function
        check_account_number_lambda = _lambda.Function(
            self,
            "HelloHandler",
            function_name="check_account_number",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda.lambda_handler"
        )

        definition = tasks.LambdaInvoke(self, 
            "Invoke Lambda - Validate account number",
            lambda_function=check_account_number_lambda,
            output_path="$.Payload",
        ).add_retry(max_attempts=3).next(
            sfn.Choice(self, "is Account number 12 bytes")
            .when(sfn.Condition.number_equals("$.statusCode", 200),
                tasks.LambdaInvoke(self, "Invoke Lambda - HelloLambda",
                    lambda_function=hello_world_lambda,
                    output_path="$.Payload",
                ).add_retry(max_attempts=3).next(
                    sfn.Succeed(self, "Success")
                )
            )
            .when(sfn.Condition.number_equals("$.statusCode", 400),
                sfn.Fail(self, "Fail")
            )
        )

        sfn.StateMachine(self, "StateMachine",
            definition=definition,
            timeout=Duration.minutes(5),
        )



