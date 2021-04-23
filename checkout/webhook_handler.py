# This file is copied from the Boutique Ado project.

from django.http import HttpResponse


class StripeWH_Handler:
    """ A classs to handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
        )
