import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AbPxfQZ-ra_NEWVqcgOr93AvNhjmB83pT2SDT1R5JSFQFB5Y-i16sQxtslsnmGmWC46ZGXqJBtWVfWHA"
        self.client_secret = "EHXeF6w4vWeaWyPDjR4GB0tEEdXAmUuNBWT5YoMeTthXdR94L9enfYWIhgUDzlVn56mRDnkRjzfFeanC"
        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret
        )
        self.client = PayPalHttpClient(self.environment)
