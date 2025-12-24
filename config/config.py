from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "memory" / "memory.db"
MODEL = "llama3.1:8b"
MEMORY_LIMIT = 12

AUDIO_FILE = BASE_DIR / "audio" / "input.wav"
SAMPLE_RATE = 16000
RECORD_SECONDS = 5
LANGUAGE = "es"

MIC_DEVICE_ID = 13

