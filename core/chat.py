from core.llm import chat as llm_chat

def chat(modo: str, mensaje: str) -> dict:
    """
    API interna para usar la IA desde cualquier sistema
    """

    if modo not in ["texto", "voz"]:
        raise ValueError("Modo inválido")

    respuesta = llm_chat(mensaje)

    return {
        "ok": True,
        "modo": modo,
        "prompt": mensaje,
        "respuesta": respuesta
    }
