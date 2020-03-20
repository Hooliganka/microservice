from aiohttp import web

from utils import get_products, response_api, db
from models import Product
from bson import ObjectId
from pydantic import ValidationError


async def products(request):
    data = []
    async for item in get_products(request):
        data.append(item)

    return response_api(data)


async def products_title(request):
    data = []
    async for item in get_products(request):
        data.append(item['title'])

    return response_api(data)


async def product(request):
    result = await db.product.find_one({'_id': ObjectId(request.match_info['id'])})
    return response_api(result)


async def create(request):
    data = await request.json()
    try:
        product = Product(**data)
    except ValidationError as error:
        raise web.HTTPBadRequest(body=error.json(), content_type='application/json')

    await db.product.insert_one(product.dict())

    return web.Response(status=201)
