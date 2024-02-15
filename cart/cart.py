from decimal import Decimal;

from store.models import Product;

class Cart():

    """
    A base Cart class, providing some default bahaviors that can be inherited or overrided, as necessary.
    """

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('skey')
        if 'sky' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart


    def add(self, product):

        """
        Adding and updating the users cart session data
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price': product.price}


        self.session.modified = True