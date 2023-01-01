from fastapi import FastAPI
import uvicorn
from server_fastapi.auto_gen import default_api
from fastapi.staticfiles import StaticFiles

## user define api
# from server_fastapi.api import api

server = FastAPI()
server.include_router(default_api)

server.mount('/', StaticFiles(directory='browser_client', html=True), name='root')

# server.include_router(api)

# uvicorn.run("server_fastapi.server:server", port=8082, reload=True)
