## Zebrand-backend-test

### Running the development environment
Do you need reate a new environment with Python 3.10 and create a table with Postgres

```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

Create file .env with credentials to use DB

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=zebrand
DB_PASSWORD=zebrand
DB_USER=zebrand
```

run commands 

```
 export $(cat .env | sed -e /^$/d -e /^#/d | xargs)
 uvicorn main:app
```

* `pytest -s -vvvv`


### Hostnames for accessing the service directly when service running in local

* Local: http://127.0.0.1:8000


### Use APP

You can show the docs to query and mutation enabled to use to run in console graphql

#### Querys

Examples: 
```
query {
    allProducts{

            id
            name
            brand
            price
            sku

        }
    }
```
```
query {
  searchProducts(sku: "item-0001"){

          id
          name
          brand
          price
          sku

      }
  }
  ```

#### Mutations

Examples: 

```
mutation{
  createProduct(
    sku:"item-001",
  brand:"SAMSUNG",
  name: "TV LED",
  price: 1200000)  
  {
    response
  }
}
```
```
mutation{updateProduct(
  sku:"item-001",
	brand: "LG"){
    response
  }}
  ```
```
mutation{deleteProduct(
  sku:"item-001"){
    response
  }}
  ```

