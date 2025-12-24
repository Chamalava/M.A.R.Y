# Voces para Piper TTS

Esta carpeta deve de contener los modelos de voz para Piper TTS, que se utilizan para la síntesis de voz (texto a voz) en M.A.R.Y.

## Instalación de Nuevas Voces

Para agregar más voces, sigue estos pasos:

1. **Instala Piper TTS**:

   ```bash
   pip install piper-tts
   ```
2. **Descarga modelos de voz** desde el [repositorio oficial de Piper](https://github.com/rhasspy/piper/releases):

   - Ve a la sección de releases y busca modelos de voz en el formato `.onnx`.
   - Descarga el archivo `.onnx` y su correspondiente `.onnx.json`.
3. **Coloca los archivos en esta carpeta** (`voices/`):

   - Ambos archivos (`.onnx` y `.onnx.json`) deben estar en el mismo directorio.
4. **Actualiza la configuración** en `config/config.py`:

   ```python
   VOICE_MODEL = BASE_DIR / "voices" / "tu_modelo.onnx"
   ```
5. **Prueba la nueva voz**:

   ```bash
   python interfaces/cli.py
   # Selecciona modo voz para probar
   ```

## Voces Disponibles en Piper

Piper ofrece voces para múltiples idiomas. Algunos ejemplos:

- Español: `es_ES-carme-high`, `es_ES-carme-medium`, `es_MX-claudia-high`, etc.
- Inglés: `en_US-amy-medium`, `en_US-john-medium`, etc.
- Otros idiomas: Francés, Alemán, Italiano, Portugués, etc.

## Nota

- Los archivos `.onnx` pueden ser bastante grandes (50-200 MB dependiendo del modelo).
- Asegúrate de tener espacio suficiente en tu disco.
- Para mejor rendimiento, usa modelos de calidad "high" o "medium" según tu hardware.
