"""Main code of the game."""
from fastapi import FastAPI, Request, WebSocket
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


@app.websocket("/")
async def main_ws_game(websocket: WebSocket):
    """
    Main WS server that contains the game.

    Parameters
    ----------
    websocket: WebSocket
        The websocket used to connect the client
    """
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
