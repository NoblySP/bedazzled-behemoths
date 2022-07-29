"""Main code of the game."""
from json import dumps
from random import random

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(name="Main game")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def main_game(request: Request):
    """
    Render the main game.

    Parameters
    ----------
    request: Request
        The request of the client
    """
    return templates.TemplateResponse("index.html", {"request": request})


rooms = []


@app.websocket("/{id}")
async def main_ws_game(websocket: WebSocket, id: int):
    """
    Main WS server that contains the game.

    Parameters
    ----------
    websocket: WebSocket
        The websocket used to connect the client
    """
    try:
        await websocket.accept()
        if id in rooms:
            error = {"rooms": rooms}
            await websocket.send_text(dumps(error))
        rooms.append(id)
        actions_HP = [
            "reduce",
            "add",
            "mult",
            "divide"
        ]
        action = {
            "action": actions_HP[round(random() * 3)],
            "to": "HP",
            "value": round(random() * 70)
        }
        await websocket.send_text(dumps(action))
        while True:
            data = await websocket.receive_text()
            print(data)
    except WebSocketDisconnect:
        print(f"disconnected {id}")
        if id in rooms:
            rooms.remove(id)
        print(rooms)
