import sounddevice as sd
import soundfile as sf
from config.config import AUDIO_FILE, RECORD_SECONDS

MIC_DEVICE_ID = 13  # tu mic
DEVICE_INFO = sd.query_devices(MIC_DEVICE_ID)
SAMPLE_RATE = int(DEVICE_INFO["default_samplerate"])

def record():
    print(f"🎙️ Escuchando a {SAMPLE_RATE} Hz...")
    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        device=MIC_DEVICE_ID
    )
    sd.wait()
    sf.write(AUDIO_FILE, audio, SAMPLE_RATE)
