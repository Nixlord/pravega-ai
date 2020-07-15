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


import json
@app.get("/hudibaba")
async def demo_creds():
    return json.loads(open("credentials.json", "r").read())


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
        response = send_text_dialogflow(data)
        await websocket.send_json(response)





if __name__ == '__main__':
    uvicorn.run(app)
