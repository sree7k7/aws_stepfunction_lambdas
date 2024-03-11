import aws_cdk as core
import aws_cdk.assertions as assertions

from testevent_rule.testevent_rule_stack import TesteventRuleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in testevent_rule/testevent_rule_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TesteventRuleStack(app, "testevent-rule")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
