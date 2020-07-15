from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


#  check if websockets can do filehandling
# i have remmoved apt buildpack will need to be restored before running open cv
# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }


@app.websocket("/ws/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


if __name__ == '__main__':
    uvicorn.run(app)
