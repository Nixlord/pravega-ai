from pathlib import Path
import subprocess
import speech_recognition as Speech
import dialogflow_v2 as dialogflow
import os
from server.hackathon import customerService, personalAssistant

SESSION_ID = 'me'

recognizer = Speech.Recognizer()


def send_text_dialogflow(text_to_be_analyzed):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = personalAssistant["filename"]
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(personalAssistant["project"], SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except:
        raise
    return {
        "text": response.query_result.query_text,
        "intent": response.query_result.intent.display_name,
        "intentConfidence": response.query_result.intent_detection_confidence,
        "fullfillment": response.query_result.fulfillment_text
    }


def convert(audio, outputPath):
    print(subprocess.run([
        'ffmpeg', '-i',
        audio.name,
        outputPath
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8"))


def send_audio_dialogflow(audio):
    # Can OOM
    output = f"{audio.name.split('.')[0]}.wav"
    convert(audio, output)
    with Speech.AudioFile(output) as source:
        audio = recognizer.record(source)

    try:
        result = recognizer.recognize_google(audio)
    except:
        result = ""

    return result


