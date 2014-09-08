__author__ = 'rafael.paiva'


class Product():

    Name = ""
    Price = 0.0
    Type_Promotion = None

    def __init__(self, name, price, type_promotion):
        self.Name = name
        self.Price = price
        self.Type_Promotion = type_promotion


class TypePromotion:

    Name = ""

    def __init__(self, name):
        self.Name = name


def register_type_promotion():
    Buy2Get1Free = TypePromotion("Buy 2 Get 1 Free")
    print(Buy2Get1Free.Name)



register_type_promotion()
#register_products()
#buy_10_candys()
