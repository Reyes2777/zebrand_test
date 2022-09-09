import graphene
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from zebrand import run
from zebrand.api.schema.mutation import Mutation
from zebrand.api.schema.query import Query

app = Starlette()
schema = graphene.Schema(query=Query, mutation=Mutation)
app.add_route(path='/', route=GraphQLApp(schema=schema, on_get=make_graphiql_handler()))


@app.on_event('startup')
async def init_db():
    await run()
