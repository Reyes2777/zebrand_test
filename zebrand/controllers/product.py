from zebrand.models import Product


class ProductController:

    _model = Product()

    async def create(self, **kwargs):
        product = await self._model.get_or_none(sku=kwargs.get('sku'))
        if not product:
            product = await self._model.create(
                sku=kwargs['sku'],
                name=kwargs['name'],
                brand=kwargs['brand'],
                price=kwargs['price'])
            return product, 'product created success'
        return product, 'product already exist'

