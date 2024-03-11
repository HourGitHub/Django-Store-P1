import stripe

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.cart import Cart

@login_required
def CartView(request):

    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    print('total')

    stripe.api_key = 'pk_test_51Ot3ZGKqHvYJjygX45bM69BDZqEpqFlr1ScQxUKm7tBYLz6x0EiZ3uHKJg66Vss4UQHnCrntm8VefjHzmNhOPgrC00v8rlgD8I'

    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

