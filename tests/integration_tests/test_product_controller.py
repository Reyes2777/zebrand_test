from pytest import mark

from zebrand.controllers.product import ProductController
from zebrand.models import Product

_create_product_success = (
    (
        {
            'sku': 'item-0001',
            'name': 'TV',
            'brand': 'samsung',
            'price': 1000000
        },
    )
)

_create_product_error = (
    (
        {
            'sku': None,
            'name': 'TV',
            'brand': 'samsung',
            'price': 1000000,
            'error': 'sku is non nullable field, but null was passed'
        }
    ),
    (
        {
            'sku': 'item-002',
            'name': None,
            'brand': 'samsung',
            'price': 1000000,
            'error': 'name is non nullable field, but null was passed'
        }
    )
)


@mark.asyncio
@mark.parametrize('params', _create_product_success)
async def test_create_product(db_transaction, params):
    product_controller = ProductController()
    product, message = await product_controller.create(
        sku=params['sku'],
        name=params['name'],
        brand=params['brand'],
        price=params['price']
    )
    assert message == 'product created success'
    assert isinstance(product, Product)


@mark.asyncio
@mark.parametrize('params', _create_product_success)
async def test_update_product(db_transaction, product_fixture, params):
    product_controller = ProductController()
    product, message = await product_controller.update(
        sku=params['sku'],
        name='TV LED 50',
        brand='SAMSUNG',
        price=1200000
    )
    assert message == 'Product update success'
    assert product.name == 'TV LED 50'
    assert product.price == 1200000
    assert isinstance(product, Product)


@mark.asyncio
@mark.parametrize('params', _create_product_success)
async def test_all_products(db_transaction, product_fixture, params):
    product_controller = ProductController()
    products, message = await product_controller.all()
    assert message == 'All objects'
    assert type(products) == list


@mark.asyncio
@mark.parametrize('params', _create_product_success)
async def test_all_search_products(db_transaction, product_fixture, params):
    product_controller = ProductController()
    products, message = await product_controller.search_product(sku=params.get('sku'))
    assert message == 'Search Success'
    assert type(products) == list


@mark.asyncio
@mark.parametrize('params', _create_product_success)
async def test_create_product_when_already_exist(db_transaction, product_fixture, params):
    product_controller = ProductController()
    product, message = await product_controller.create(
        sku=params['sku'],
        name=params['name'],
        brand=params['brand'],
        price=params['price']
    )
    assert message == 'product already exist'
    assert isinstance(product, Product)


@mark.asyncio
@mark.parametrize('params', _create_product_error)
async def test_create_product_invalid_params(db_transaction, params):
    product_controller = ProductController()
    product, message = await product_controller.create(
        sku=params['sku'],
        name=params['name'],
        brand=params['brand'],
        price=params['price']
    )
    assert message == params.get('error')
