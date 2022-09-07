from tortoise import Model, fields


class Product(Model):

    brand = fields.TextField()
    id = fields.IntField(pk=True)
    name = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    sku = fields.TextField()
