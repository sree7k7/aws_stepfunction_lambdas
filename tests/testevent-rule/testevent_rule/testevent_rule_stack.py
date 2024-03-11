from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_events as events
import aws_cdk.aws_iam as iam
from constructs import Construct

class TesteventRuleStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Resources
    eventsEventBus00default00U5kFh = events.CfnEventBus(self, 'EventsEventBus00default00U5kFH',
          tags = [
          ],
          name = 'default',
        )
    eventsEventBus00default00U5kFh.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamManagedPolicy00policyserviceroleAmazonEventBridgeInvokeStepFunctions55938312500wTcgb = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleAmazonEventBridgeInvokeStepFunctions55938312500wTCGB',
          managed_policy_name = 'Amazon_EventBridge_Invoke_Step_Functions_559383125',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  'arn:aws:states:eu-central-1:619831221558:stateMachine:StateMachine2E01A3A5-fu8yG6kEbNY8',
                ],
                'Action': [
                  'states:StartExecution',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'Amazon_EventBridge_Invoke_Step_Functions_559383125',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleAmazonEventBridgeInvokeStepFunctions55938312500wTcgb.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamRole00AmazonEventBridgeInvokeStepFunctions55938312500LlwSx = iam.CfnRole(self, 'IAMRole00AmazonEventBridgeInvokeStepFunctions55938312500LlwSX',
          path = '/service-role/',
          managed_policy_arns = [
            iamManagedPolicy00policyserviceroleAmazonEventBridgeInvokeStepFunctions55938312500wTcgb.ref,
          ],
          max_session_duration = 3600,
          role_name = 'Amazon_EventBridge_Invoke_Step_Functions_559383125',
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'events.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRole00AmazonEventBridgeInvokeStepFunctions55938312500LlwSx.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    eventsRule00ruletriggerSateMachine00kEDy9 = events.CfnRule(self, 'EventsRule00ruletriggerSateMachine00kEDy9',
          event_bus_name = eventsEventBus00default00U5kFh.ref,
          event_pattern = {
            'detail-type': [
              'AWS API Call via CloudTrail',
            ],
            'source': [
              'aws.s3',
            ],
            'detail': {
              'eventSource': [
                's3.amazonaws.com',
              ],
              'requestParameters': {
                'bucketName': [
                  'sran11-sfn-tutorial',
                ],
              },
              'eventName': [
                'PutObject',
              ],
            },
          },
          targets = [
            {
              'arn': 'arn:aws:states:eu-central-1:619831221558:stateMachine:StateMachine2E01A3A5-fu8yG6kEbNY8',
              'roleArn': iamRole00AmazonEventBridgeInvokeStepFunctions55938312500LlwSx.attr_arn,
              'id': 'Id94f06347-4d58-44f9-be1f-f0584b846b4c',
            },
          ],
          id = 'triggerSateMachine',
          state = 'ENABLED',
          name = 'triggerSateMachine',
        )
    eventsRule00ruletriggerSateMachine00kEDy9.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN


