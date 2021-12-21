import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

app = web.Application()
#app.router.add_routes([web.get('/', index),
#                       web.get('/hello/{name}', hello)])
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/hello/{name}', hello)
web.run_app(app, host='127.0.0.1', port=8000)