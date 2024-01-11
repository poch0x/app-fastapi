from fastapi import APIRouter, Path, Query

from models.product import Product

router = APIRouter()


products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 20,
        "stock": 10
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 30,
        "stock": 50
    },
]


@router.get('/products')
def get_products():
    return products


@router.get('/products/{id}')
def get_product(id: int = Path(gt=0)):
    return list(filter(lambda item: item['id'] == id, products)) 


# products/?stock=10 -> parametros query
@router.get('/products/')
def get_products_by_stock(stock: int, price: float = Query(gt=0)):
    return list(filter(lambda item: item['stock'] == stock and 
                            item['price'] == price, products)) 
    


@router.post('/products')
def create_product(product: Product):
    products.append(product)
    return products


@router.put('/products/{id}')
def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]['name'] = product.name
            products[index]['price'] = product.price
            products[index]['stock'] = product.stock
    return products


@router.delete('/products/{id}')
def delete_product(id: int):
    for item in products:
        if item['id'] == id:
            products.remove(item)    
    return products

