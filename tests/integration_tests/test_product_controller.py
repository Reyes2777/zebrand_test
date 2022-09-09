from pytest import mark

from zebrand.controllers.product import ProductController

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
