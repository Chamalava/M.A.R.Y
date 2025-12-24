from fastapi import FastAPI
from pydantic import BaseModel
from core.chat import chat
from memory.db import init_db

app = FastAPI(title="IA Local API")

init_db()

class ChatRequest(BaseModel):
    modo: str
    mensaje: str

@app.post("/chat")
def chat_endpoint(data: ChatRequest):
    """
    Endpoint para manejar solicitudes de chat.
    """
    result = chat(
        modo=data.modo, 
        mensaje=data.mensaje
    )
    
    return result