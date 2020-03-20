from views import (
    products,
    product,
    create,
    products_title
)

patterns = [
    ['GET', '/api/products_title/', products_title],
    ['GET', '/api/products/', products],
    ['GET', '/api/product/{id}/', product],
    ['POST', '/api/create/', create],
]
