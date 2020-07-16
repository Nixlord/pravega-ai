import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable
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

def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        with NamedTemporaryFile(delete=False, suffix="3gp") as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path

def get_file(upload_file: UploadFile):
    tmp = NamedTemporaryFile(delete=False, suffix=".3gp", prefix="snd_")
    shutil.copyfileobj(upload_file.file, tmp)
    upload_file.file.close()
    return tmp


@app.post("/audio-file/")
def handle_audio_upload(file: UploadFile = File(...)):
    """
     curl -X POST
        -H 'Accept: application/json'
        -H 'Content-Type: multipart/form-data; charset=utf-8'
        -F file="@./something"
        http://localhost:8000/audio-file/
    """
    tmpFile = get_file(file)
    response = {
        "content": send_audio_dialogflow(tmpFile)
    }
    tmpFile.close()
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
