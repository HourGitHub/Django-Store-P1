# import sys

# from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


# class PayPalClient:
#     def __init__(self):
#         self.client_id = "AbPxfQZ-ra_NEWVqcgOr93AvNhjmB83pT2SDT1R5JSFQFB5Y-i16sQxtslsnmGmWC46ZGXqJBtWVfWHA"
#         self.client_secret = "EHXeF6w4vWeaWyPDjR4GB0tEEdXAmUuNBWT5YoMeTthXdR94L9enfYWIhgUDzlVn56mRDnkRjzfFeanC"
#         self.environment = SandboxEnvironment(
#             client_id=self.client_id, client_secret=self.client_secret
#         )
#         self.client = PayPalHttpClient(self.environment)


from django.shortcuts import render
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


def payment_selection(request):
    client_id = "AbPxfQZ-ra_NEWVqcgOr93AvNhjmB83pT2SDT1R5JSFQFB5Y-i16sQxtslsnmGmWC46ZGXqJBtWVfWHA"
    client_secret = "EHXeF6w4vWeaWyPDjR4GB0tEEdXAmUuNBWT5YoMeTthXdR94L9enfYWIhgUDzlVn56mRDnkRjzfFeanC"
    environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)

    return render(request, "payment_selection.html", {"paypal_client": client})
