import asyncio
import os
import subprocess

import asyncpg
from pytest import fixture
from pytest_asyncio import fixture as async_fixture

from tests.factories import ProductFactory
from zebrand import run, settings


@async_fixture(scope='session')
async def create_db():
    subprocess.call(['psql', '-U', settings.DB_USER, '-w', '-h', settings.DB_HOST,
                     '-d', settings.DB_NAME, '-f', f'{os.path.dirname(__file__)}/db.sql'])
    settings.DB_NAME = settings.DB_NAME + '_test'
    await run(generate_schemas=True)


@fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@async_fixture
async def db_connection(create_db, event_loop):
    print('creating db connection with', settings.DB_NAME)
    connection = await asyncpg.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        password=settings.DB_PASSWORD,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        timeout=5
    )
    yield connection
    await connection.close()


@async_fixture
async def db_transaction(event_loop, create_db, db_connection):
    yield
    print('doing rollback...')
    await db_connection.execute('TRUNCATE product CASCADE;')


@async_fixture
async def product_fixture(db_transaction):
    product = ProductFactory.build()
    await product.save()

