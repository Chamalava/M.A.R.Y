# M.A.R.Y - Asistente IA Local

Este es mi proyecto M.A.R.Y (Modular Autonomous Reasoning You), un asistente de inteligencia artificial modular y autónomo que funciona completamente offline en entornos locales. Desarrollado en Python, combina modelos de lenguaje, memoria persistente y procesamiento de audio para ofrecer interacciones naturales y privadas.

## Funcionalidades Principales

- **Modelo Local**: Usa Ollama con Llama 3.1 para generar respuestas inteligentes basadas en contexto.
- **Memoria Persistente**: Almacena conversaciones en SQLite para mantener el historial y coherencia.
- **Audio (STT/TTS)**: Transcribe voz con Whisper y sintetiza respuestas con Piper TTS en español.
- **Modos de Interacción**: CLI con opciones de texto o voz.
- **API REST**: Endpoint simple con FastAPI para integraciones.

## Instalación

1. Instala dependencias: `pip install -r requirements.txt`
2. Configura Ollama y Piper TTS.
3. Ejecuta: `python interfaces/cli.py` para CLI, o `uvicorn api:app --reload` para API.

## Uso

- En CLI, elige modo texto (`t`) o voz (`v`) para chatear.
- API: POST a `/chat` con JSON `{"modo": "texto", "mensaje": "Hola"}`.

Configurable en `config/config.py`. Ideal para privacidad y uso técnico en Arch Linux.