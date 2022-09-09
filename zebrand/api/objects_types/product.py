import graphene


class ProductObjectType(graphene.ObjectType):
    id = graphene.ID()
    sku = graphene.String()
    name = graphene.String()
    brand = graphene.String()
    price = graphene.Decimal()

