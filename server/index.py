from fastapi import FastAPI, WebSocket
import uvicorn

from server.hackathon.getTextResponse import send_text_dialogflow

app = FastAPI()

#  check if websockets can do filehandling
# i have remmoved apt buildpack will need to be restored before running open cv
# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }


@app.get("/textDialog")
async def textDialog():
    text = 'i am not satisfied'
    return send_text_dialogflow(text)


# HTTP file upload, return filename, then send here.

@app.websocket("/ws/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")





if __name__ == '__main__':
    uvicorn.run(app)
