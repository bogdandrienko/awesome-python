from sanic import Sanic
from sanic.response import text
from sanic import Request, Websocket
import random

app = Sanic("MyHelloWorldApp")


# app.static("/", "/path/to/index.html")
# app.static("/uploads/", "/path/to/uploads/")

@app.get("/")
async def hello_world(request):
    val = random.randint(1, 100)
    return text(f"Hello, world.{val}")


@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    async for msg in ws:
        await ws.send(msg)

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True,
        auto_reload=True,
    )
