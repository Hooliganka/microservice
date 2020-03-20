import yaml
import json

from aiohttp import web
from bson import ObjectId
from motor import motor_asyncio

from models import Product

with open("config.yml", 'r') as ymlfile:
    CONFIG = yaml.load(ymlfile, Loader=yaml.FullLoader)

client = motor_asyncio.AsyncIOMotorClient(
    CONFIG['mongo']['host'],
    CONFIG['mongo']['port'],
    username=CONFIG['mongo']['username'],
    password=CONFIG['mongo']['password']
)
db = client.test_database
collection = db.product


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def get_row(get: dict):
    result = {}
    _product = Product.__fields__

    for item in get.keys():
        if '.' in item:
            temp = item.split('.')
            field = _product.get(temp[0])
            data_type = field.type_.__fields__.get(temp[1]).type_
        else:
            data_type = _product.get(item).type_

        result.update({
            item: data_type(get[item])
        })

    return result


def response_api(data):
    return web.json_response(data=data, dumps=JSONEncoder().encode)


def get_products(request):
    _get = request.rel_url.query
    _filter = {}
    if _get:
        try:
            _filter.update(get_row(_get))
        except ValueError:
            raise web.HTTPBadRequest(content_type='application/json')

    return db.product.find(_filter)
