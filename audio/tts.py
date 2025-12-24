import subprocess
import tempfile
import os
from config.config import BASE_DIR

PIPER_BIN = "piper-tts"
VOICE_MODEL = BASE_DIR / "voices" / "es_MX-claudia-high.onnx"

def speak(text: str):
    if not text.strip():
        return

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav_path = f.name

    try:
        subprocess.run(
            [
                PIPER_BIN,
                "--model", VOICE_MODEL,
                "--output_file", wav_path
            ],
            input=text.encode("utf-8"),
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        subprocess.run(
            ["aplay", wav_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)
