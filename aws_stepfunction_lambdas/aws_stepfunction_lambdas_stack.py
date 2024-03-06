from aws_cdk import (
    Stack,
    Duration
)
from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks


class AwsStepfunctionLambdasStack(Stack):
    """
    A CDK stack that creates a Step Function with Lambda functions.

    This stack creates a Step Function state machine and adds Lambda functions with choice to the state machine.
    The state machine includes two Lambda functions: HelloWorld and CheckAccountNumber.
    The HelloWorld Lambda function is invoked if the account number validation is successful.
    The CheckAccountNumber Lambda function is invoked to validate the account number.
    The state machine definition includes retries and choice conditions based on the status code returned by the CheckAccountNumber Lambda function.
    The state machine has a timeout of 5 minutes.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Step Function state machine
        # and add the lambda functions with choice to the state machine

        # Define the HelloWorld Lambda function
        hello_world_lambda = _lambda.Function(
            self,
            "HelloWorldHandler",
            function_name="hello_world",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("lambda"),
            handler="helloworld.lambda_handler"
        )

        # Define the CheckAccountNumber Lambda function
        check_account_number_lambda = _lambda.Function(
            self,
            "HelloHandler",
            function_name="check_account_number",
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda.lambda_handler"
        )

        # Define the state machine definition
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

        # Create the Step Function state machine
        sfn.StateMachine(self, "StateMachine",
            definition=definition,
            timeout=Duration.minutes(5),
        )


