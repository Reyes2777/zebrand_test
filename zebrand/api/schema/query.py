import graphene

from zebrand.api.objects_types.product import ProductObjectType
from zebrand.controllers.product import ProductController


class Query(graphene.ObjectType):
    search_products = graphene.List(
        ProductObjectType,
        sku=graphene.String(),
        name=graphene.String(),
        brand=graphene.String()
        )
    all_products = graphene.List(ProductObjectType)

    @staticmethod
    async def resolve_search_products(root, info, **kwargs):
        product_controller = ProductController()
        products, message = await product_controller.search_product(**kwargs)
        return products

    @staticmethod
    async def resolve_all_products(root, info):
        product_controller = ProductController()
        products, message = await product_controller.all()
        return products
