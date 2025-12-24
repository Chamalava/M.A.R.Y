from core.llm import chat
from audio.audio import record
from audio.stt import transcribe
from audio.tts import speak

def text_mode():
    print("Modo de texto. Escribe 'q' para salir.")
    while True:
        user_input = input("Tú: ").strip().lower()
                
        if user_input in ["q", "quit", "exit"]:
            break
        
        reply = chat(user_input)
        print(f"Asistente: \n{reply}\n")

def voice_mode():
    print("Modo de voz. Escribe 'q' para salir.")
    while True:
        record()
        user_input = transcribe()
        print(f"Tú: {user_input}")
        
        if user_input.lower() in ["q", "quit", "exit"]:
            break
        
        reply = chat(user_input)
        print(f"Asistente: \n{reply}\n")
        speak(reply)

        