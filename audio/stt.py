import whisper
from config.config import AUDIO_FILE, LANGUAGE

model = whisper.load_model("base")

def transcribe():
    result = model.transcribe(str(AUDIO_FILE), language=LANGUAGE)
    return result["text"].strip()