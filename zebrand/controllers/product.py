from zebrand.models import Product


class ProductController:

    _model = Product()

    async def create(self, **kwargs):
        product = await self._model.get_or_none(sku=kwargs.get('sku'))
        if not product:
            try:
                product = await self._model.create(
                    sku=kwargs['sku'],
                    name=kwargs['name'],
                    brand=kwargs['brand'],
                    price=kwargs['price'])
            except Exception as error:
                return None, error.args[0]
            return product, 'product created success'
        return product, 'product already exist'

    async def delete(self, sku: str):
        product = await self._model.get_or_none(sku=sku)
        if not product:
            return None, 'Item not exist'
        return await product.delete(), 'Item delete success'

    async def update(self, **kwargs):
        product = await self._model.get(sku=kwargs.get('sku'))
        if not product:
            return None, 'Item not exist'
        await product.update_from_dict(kwargs)
        return product, 'Product update success'

    async def all(self):
        products = await self._model.all()
        return products, 'All objects'

    async def search_product(self, **kwargs):
        products = await self._model.filter(**kwargs)
        if products:
            return products, 'Search Success'
        return [], 'Dont exist items with this params'
