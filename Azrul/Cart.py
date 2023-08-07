

class Cart:
    # count = 0
    def __init__(self, product_id, product_name, product_price, product_size, product_colour, product_quantity):
        # Cart.count += 1
        # self.__product_id = Cart.count
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price
        self.__product_size = product_size
        self.__product_colour = product_colour
        self.__product_quantity = product_quantity



    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__product_price

    def get_product_size(self):
        return self.__product_size

    def get_product_colour(self):
        return self.__product_colour

    def get_product_quantity(self):
        return self.__product_quantity




    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_product_price(self, product_price):
        self.__product_price = product_price

    def set_product_size(self, product_size):
        self.__product_size = product_size

    def set_product_colour(self, product_colour):
        self.__product_colour = product_colour

    def set_product_quantity(self, product_quantity):
        self.__product_quantity = product_quantity


def add_product_to_cart(product, cart_db):
    # Retrieve the cart dictionary from the database
    cart_dict = cart_db.get('cart', {})

    # Generate a unique key for the new product using its product_id
    product_key = product.get_product_id()

    # Check if the product is already in the cart
    if product_key in cart_dict:
        # If the product is already in the cart, update its quantity
        cart_dict[product_key]['quantity'] += product.get_product_quantity()
    else:
        # If the product is not in the cart, add it as a new entry
        cart_dict[product_key] = {
            'name': product.get_product_name(),
            'price': product.get_product_price(),
            'size': product.get_product_size(),
            'colour': product.get_product_colour(),
            'quantity': product.get_product_quantity()
        }

    # Update the cart dictionary in the database
    cart_db['cart'] = cart_dict