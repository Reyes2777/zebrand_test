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


class DeleteProductMutation(graphene.Mutation):

    response = graphene.String()

    class Arguments:
        sku = graphene.String()

    async def mutate(self, info, sku):
        product_controller = ProductController()
        product, message = await product_controller.delete(
            sku=sku
        )
        return CreateProductMutation(response=message)


class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
    delete_product = DeleteProductMutation.Field()


class UpdateProductMutation(graphene.Mutation):

    response = graphene.String()

    class Arguments:
        sku = graphene.String()
        name = graphene.String()
        brand = graphene.String()
        price = graphene.String()

    async def mutate(self, info, **kwargs):
        product_controller = ProductController()
        product, message = await product_controller.update(**kwargs)
        return CreateProductMutation(response=message)


class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
    delete_product = DeleteProductMutation.Field()
    update_product = UpdateProductMutation.Field()
