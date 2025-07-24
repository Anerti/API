import json
from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import List
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root(request: Request):
    required_header = request.headers.get("Accept")
    if (required_header == "text/html" or required_header == "text/plain"):
        required_key = request.headers.get("x-api-key")
        if required_key == "12345678":
            with open("welcome.html", "r", encoding="utf-8") as file:
                html_content = file.read()
            return Response(content=html_content, status_code=200, media_type="text/html")
        return JSONResponse(content={"message": "Unknown api key"}, status_code=403)
    return JSONResponse(content={"message": "only 'text/plain' or 'text/html' are supported"}, status_code=400)

class EventModel(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str

event_store: List[EventModel] = []

def serialized_stored_events():
    events_converted = []
    for event in event_store:
        events_converted.append(event.model_dump())
    return events_converted

@app.get("/events")
def list_events():
    return serialized_stored_events()

@app.post("/events")
def add_event(new_event: EventModel):
    event_store.append(new_event)
    return event_store

@app.put("/events")
def edit_event(data: EventModel):
    update = False
    for event in event_store:
        if data.name == event:
            event = data
            update = True
    if not update:
        return add_event(EventModel)
    return event_store


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("not_found.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

