from pathlib import Path

import speech_recognition as Speech
import dialogflow_v2 as dialogflow
from fastapi import File, UploadFile

DIALOGFLOW_PROJECT_ID = 'hackethon-283217'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

recognizer = Speech.Recognizer()


def send_text_dialogflow(text_to_be_analyzed):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except:
        raise
    return {
        "text": response.query_result.query_text,
        "intent": response.query_result.intent.display_name,
        "intent_confidence": response.query_result.intent_detection_confidence,
        "fullfillment": response.query_result.fulfillment_text
    }


def send_audio_dialogflow(audio: File):
    # Can OOM
    with Speech.AudioFile(audio) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_google(audio)
