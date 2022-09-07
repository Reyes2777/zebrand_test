import graphene

from zebrand.controllers.product import ProductController


class CreateProductMutation(graphene.Mutation):

    response = graphene.String()

    class Arguments:
        sku = graphene.String()
        name = graphene.String()
        brand = graphene.String()
        price = graphene.Int()

    async def mutate(self, info, sku, name, brand, price):
        product_controller = ProductController()
        product, message = await product_controller.create(
            sku=sku,
            name=name,
            brand=brand,
            price=price
        )
        return CreateProductMutation(response=message)


class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
