from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/health')
async def hello(request):
    return web.HTTPOk()

@routes.get('/')
async def hello(request):
    return web.json_response({"Choo Choo": "Welcome to your aiohttp app"})

async def my_web_app():
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == "__main__":
    web.run_app(my_web_app())