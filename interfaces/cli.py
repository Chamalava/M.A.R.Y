from memory.db import init_db
from core.modes import text_mode, voice_mode

def main():
    init_db()
    print("\n=== Asistente de IA Local ===\n")

    while True:
        mode = input("⌨️ [t] texto | 🎙️ [v] voz | salir: ").strip().lower()
        
        if mode in ["q", "quit", "exit", "salir"]:
            print("Adiós!")
            break
        
        if mode == "t":
            text_mode()
        elif mode == "v":
            voice_mode()
        else:
            print("Opción no válida. Intenta de nuevo.\n")
            
if __name__ == "__main__":
    main()