# import stripe
# from django.http.response import HttpResponse
# from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic.base import TemplateView

from cart.cart import Cart
from orders.views import payment_confirmation


def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def CartView(request):

    # cart = Cart(request)
    # total = str(cart.get_total_price())
    # total = total.replace('.', '')
    # total = int(total)

    # stripe.api_key = 'sk_test_51Ot3ZGKqHvYJjygXWaiRvEIlASXd412WQhu7Ge1fw2AzJmgnDnZZU7Ggx2laeZz0Ao0fVGL7dWs0yGyaFJJJWLz300T2uFJgi0'

    # intent = stripe.PaymentIntent.create(
    #     amount=total,
    #     currency='gbp',
    #     metadata={'userid': request.user.id}
    # )

    # return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
    return render(request, 'payment/payment_form.html')

# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     event = None

#     try:
#         event = stripe.Event.construct_from(
#             json.loads(payload), stripe.api_key
#         )
#     except ValueError as e:
#         print(e)
#         return HttpResponse(status=400)

#     # Handle the event
#     if event.type == 'payment_intent.succeeded':
#         payment_confirmation(event.data.object.client_secret)

#     else:
#         print('Unhandled event type {}'.format(event.type))

#     return HttpResponse(status=200)