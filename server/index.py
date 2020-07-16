from fastapi import FastAPI, WebSocket, UploadFile, File
import uvicorn

from server.hackathon.getTextResponse import send_text_dialogflow, send_audio_dialogflow

app = FastAPI()

# check if websockets can do filehandling
# i have remmoved apt buildpack will need to be restored before running open cv
# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }


@app.get("/textDialog")
async def text_dialog():
    text = 'i am not satisfied'
    return send_text_dialogflow(text)


# HTTP file upload, return filename, then send here.


@app.post("/audio-file/")
async def handle_audio_upload(file: UploadFile = File(...)):
    """
     curl -X POST
        -H 'Accept: application/json'
        -H 'Content-Type: multipart/form-data; charset=utf-8'
        -F file="@./something"
        http://localhost:8000/audio-file/
    """
    response = {
        "filename": file.filename
        # "content": send_audio_dialogflow(file)
    }
    print(response)
    return response


@app.websocket("/ws/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = send_text_dialogflow(data)
        await websocket.send_json(response)





if __name__ == '__main__':
    uvicorn.run(app)
