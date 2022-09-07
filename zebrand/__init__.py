import os
from tortoise import Tortoise


async def run(generate_schemas=False):
    await Tortoise.init(
        config={
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        'host': os.environ['DB_HOST'],
                        'port': os.environ['DB_PORT'],
                        'user': os.environ['DB_USER'],
                        'password': os.environ['DB_PASSWORD'],
                        'database': os.environ['DB_NAME']
                    }
                }
            },
            'apps': {
                'zebrand': {
                    'models': ['zebrand.models'],
                    'default_connection': 'default'
                }
            }
        }
    )
    if generate_schemas:
        await Tortoise.generate_schemas()
