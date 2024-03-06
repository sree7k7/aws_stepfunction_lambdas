import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_stepfunction_lambdas.aws_stepfunction_lambdas_stack import AwsStepfunctionLambdasStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_stepfunction_lambdas/aws_stepfunction_lambdas_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsStepfunctionLambdasStack(app, "aws-stepfunction-lambdas")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
