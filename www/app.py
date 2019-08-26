import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# old method
# def index(request):
#     return web.Response(body=b'<h1>TEST</h1/>', content_type='text/html')
#
# @asyncio.coroutine
# def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
#     logging.info('server starteed at http://127.0.0.1:9000...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

# mew method
async def index(request):
    return web.Response(text='awsome')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='127.0.0.1', port=9000)
