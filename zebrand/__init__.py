import os
from tortoise import Tortoise

from zebrand import settings


async def run(generate_schemas=False):
    await Tortoise.init(
        config={
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        'host': settings.DB_HOST,
                        'port': settings.DB_PORT,
                        'user': settings.DB_USER,
                        'password': settings.DB_PASSWORD,
                        'database': settings.DB_NAME
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
