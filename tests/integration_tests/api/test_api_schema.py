from pytest import mark


@mark.skip(reason='Solve how run async client graphql with graphene 3.1.1')
@mark.asyncio
async def test_query_search_products(db_transaction, product_fixture, graph_client, event_loop):
    query = '''
        query {
            searchProducts(sku: "item-0001"){
                    id
                    name
                    brand
                    price
                    sku
                }
            }'''
    result = graph_client.execute(query)
    assert result == {
        "data": {
            "searchProducts": [
              {
                "id": "13",
                "name": "TV",
                "brand": "samsung",
                "price": "1000000.00",
                "sku": "item-0001"
              }
            ]
          }
        }


@mark.skip(reason='Solve how run async client graphql with graphene 3.1.1')
@mark.asyncio
async def test_query_all_products(db_transaction, product_fixture, graph_client, event_loop):
    query = '''
        query {
            allProducts{
                    id
                    name
                    brand
                    price
                    sku
                }
            }'''
    result = graph_client.execute(query)
    assert result == {
        "data": {
            "allProducts": [
              {
                "id": "13",
                "name": "TV",
                "brand": "samsung",
                "price": "1000000.00",
                "sku": "item-0001"
              }
            ]
          }
    }



