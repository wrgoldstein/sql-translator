from sanic import Sanic, response
import sqlglot

app = Sanic("sqlglot-online")
app.static("/", "dist/")

@app.get("/")
async def hello_world(request):
    return await response.file("dist/index.html")

@app.post("/t")
async def data(request):
    print(request.json)
    q = request.json["q"]
    read = request.json["read"]
    write = request.json["write"]
    print(request.json)
    transpiled = sqlglot.transpile(q, read=read, write=write, pretty=True)[0]
    print(transpiled)
    return response.json(dict(transpiled=transpiled))
