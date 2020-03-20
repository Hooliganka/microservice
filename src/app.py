import argparse

from aiohttp import web
from urls import patterns

routes = web.RouteTableDef()


app = web.Application()
app.add_routes([web.route(*item) for item in patterns])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", default=8080)
    parser.add_argument("-ip", default='0.0.0.0')
    args = parser.parse_args()
    web.run_app(app, host=args.ip, port=args.port)
