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
