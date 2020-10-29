from aws_cdk.core import Stack

from b_cfn_twilio_workspace.function import TwilioWorkspaceSingletonFunction
from b_cfn_twilio_workspace.resource import TwilioWorkspaceResource


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        function = TwilioWorkspaceSingletonFunction(
            scope=self,
            name='TestingFunction',
            twilio_account_sid='Test1',
            twilio_auth_token='Test2'
        )

        TwilioWorkspaceResource(
            scope=self,
            workspace_function=function,
            workspace_name='TestWorkspace'
        )
