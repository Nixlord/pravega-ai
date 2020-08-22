import json
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable
from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from server.hackathon.getTextResponse import customer_service_bot, send_audio_dialogflow, personal_assistant_bot

app = FastAPI()

# Remove localhost and find a better method.
origins = [
    "https://shibasis-patnaik.web.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }



@app.get("/customerDialog")
async def text_dialog():
    text = 'i am not satisfied'
    return customer_service_bot(text)


@app.get("/personalDialog")
async def personal_dialog():
    text = 'I want to buy a black t-shirt'
    return personal_assistant_bot(text)


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
        text = await websocket.receive_text()
        data = json.loads(text)
        print(data)
        if data["to"] == "PERSONAL_ASSISTANT":
            bot = personal_assistant_bot
        elif data["to"] == "CUSTOMER_SERVICE":
            bot = customer_service_bot

        results = {}
        try:
            results = bot(data["text"])
        except:
            pass

        await websocket.send_json(results)

if __name__ == '__main__':
    uvicorn.run(app)
