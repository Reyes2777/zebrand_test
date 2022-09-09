import graphene

from zebrand.api.schema.mutation import Mutation
from zebrand.api.schema.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
