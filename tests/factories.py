import factory

from zebrand.models import Product


class ProductFactory(factory.Factory):
    sku = 'item-0001'
    name = 'TV LED'
    brand = 'SAMSUNG'
    price = 1200000

    class Meta:
        model = Product
