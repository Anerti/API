import json
from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import List
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello():
        return Response(content=f"Hello world", status_code=200)

@app.get("/welcome")
def welcoming(request: Request, name: str = "Undefined"):
    return Response(content=f"Welcome {name}", status_code=200)

