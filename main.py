import graphene
from graphene import ObjectType
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from zebrand import run
from zebrand.api.schema.mutation import Mutation


class User(ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(ObjectType):
    me = graphene.Field(User, name=graphene.String(default_value="World"))

    @staticmethod
    def resolve_me(root, info, name):
        return {'id': 'jonathan', 'name': name}


app = Starlette()
schema = graphene.Schema(query=Query, mutation=Mutation)
app.add_route(path='/', route=GraphQLApp(schema=schema, on_get=make_graphiql_handler()))


@app.on_event('startup')
async def init_db():
    await run()
