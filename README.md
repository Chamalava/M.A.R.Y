# M.A.R.Y - Asistente IA Local

Este es mi proyecto M.A.R.Y (Modular Autonomous Reasoning You), un asistente de inteligencia artificial modular y autónomo que funciona completamente offline en entornos locales. Desarrollado en Python, combina modelos de lenguaje, memoria persistente y procesamiento de audio para ofrecer interacciones naturales y privadas.

## Arquitectura del Proyecto

El proyecto está organizado en módulos para facilitar la mantenibilidad y extensibilidad:

- **`api.py`**: API REST con FastAPI para integraciones externas.
- **`core/`**: Núcleo del asistente.
  - `chat.py`: Interfaz interna para chat.
  - `llm.py`: Integración con Ollama para modelos de lenguaje.
  - `modes.py`: Modos de interacción (texto y voz).
  - `system_prompt.py`: Prompt del sistema que define la personalidad.
- **`config/`**: Configuración centralizada.
- **`interfaces/`**: Interfaces de usuario.
  - `cli.py`: Interfaz de línea de comandos.
- **`memory/`**: Gestión de memoria persistente con SQLite.
- **`audio/`**: Procesamiento de audio.
  - `stt.py`: Speech-to-Text con Whisper.
  - `tts.py`: Text-to-Speech con Piper TTS.
  - `audio.py`: Utilidades de audio.
- **`voices/`**: Modelos de voz para TTS (ver `voices/README.md`).
- **`tests/`**: Pruebas básicas.

## Funcionalidades Principales

### Modelo de Lenguaje Local
- Utiliza Ollama con el modelo `llama3.1:8b` (configurable).
- Genera respuestas basadas en el contexto histórico y el prompt del sistema.
- El prompt define una personalidad técnica, en español latino, concisa y útil.

### Memoria Persistente
- Almacena conversaciones en SQLite (`memory/memory.db`).
- Limita el historial a 12 mensajes por defecto para eficiencia.
- Carga contexto automáticamente en cada interacción.

### Procesamiento de Audio
- **STT**: Transcribe audio grabado (5 segundos por defecto) con Whisper en español.
- **TTS**: Sintetiza respuestas en voz con Piper TTS usando modelos `.onnx`.
- Grabación desde micrófono configurable.

### Modos de Interacción
- **Texto**: Chat textual en terminal.
- **Voz**: Ciclo completo: grabar → transcribir → responder → sintetizar voz.

### API REST
- Endpoint `/chat` para solicitudes POST con JSON: `{"modo": "texto", "mensaje": "Hola"}`.
- Respuesta: `{"ok": true, "modo": "texto", "prompt": "...", "respuesta": "..."}`.

## Instalación

### Requisitos Previos
- Python 3.8+
- Ollama instalado y modelo `llama3.1:8b` descargado.
- Piper TTS instalado.
- Sistema Linux (probado en Arch Linux).

### Pasos
1. Clona el repositorio:
   ```bash
   git clone <url-del-repo>
   cd M.A.R.Y
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Instala y configura Ollama:
   ```bash
   # Instala Ollama (ver https://ollama.ai)
   ollama pull llama3.1:8b
   ```

4. Instala Piper TTS y voces:
   ```bash
   pip install piper-tts
   # Descarga voces en voices/ (ver voices/README.md)
   ```

5. Inicializa la base de datos:
   ```bash
   python -c "from memory.db import init_db; init_db()"
   ```

## Configuración

Edita `config/config.py` para personalizar:
- `MODEL`: Modelo de Ollama (ej. "llama3.1:8b").
- `MEMORY_LIMIT`: Número de mensajes en memoria (ej. 12).
- `LANGUAGE`: Idioma para STT (ej. "es").
- `RECORD_SECONDS`: Duración de grabación (ej. 5).
- `VOICE_MODEL`: Ruta al modelo de voz (ej. `BASE_DIR / "voices" / "es_MX-claudia-high.onnx"`).
- `MIC_DEVICE_ID`: ID del dispositivo de micrófono.

## Uso

### Interfaz CLI
```bash
python interfaces/cli.py
```
- Selecciona `t` para texto, `v` para voz, `q` para salir.
- En modo texto: Escribe mensajes.
- En modo voz: Habla y escucha respuestas.

### API
```bash
uvicorn api:app --reload
```
Ejemplo de solicitud:
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"modo": "texto", "mensaje": "Hola, ¿cómo estás?"}'
```

### Ejemplos
- **Chat textual**: `python interfaces/cli.py` → `t` → "Explica Python" → Respuesta impresa.
- **Chat por voz**: `python interfaces/cli.py` → `v` → Habla → Escucha respuesta.
- **API**: Integra en scripts o apps para automatización.

## Solución de Problemas

- **Error en Ollama**: Asegúrate de que el modelo esté descargado (`ollama pull llama3.1:8b`).
- **Audio no funciona**: Verifica dispositivo de micrófono en `config.py` y que Piper esté instalado.
- **Base de datos**: Si hay errores, borra `memory/memory.db` y reinicializa.
- **Dependencias**: Usa un entorno virtual para evitar conflictos.

## Contribución

1. Forkea el repo.
2. Crea una rama para tu feature.
3. Haz commits descriptivos.
4. Envía un PR con descripción detallada.

## Licencia

Ver `M.A.R.Y/LICENSE` para detalles.

## Notas Finales

M.A.R.Y está diseñado para privacidad total (offline) y uso técnico. Si encuentras bugs o tienes ideas, abre un issue. ¡Disfruta explorando IA local!