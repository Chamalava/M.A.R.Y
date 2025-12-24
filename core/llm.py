from core.system_prompt import SYSTEM_PROMPT
from memory.db import load_memory, save_memory
import ollama
from config.config import MODEL, MEMORY_LIMIT

def chat(user_msg):
    past = load_memory(MEMORY_LIMIT)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    for role, content in past:
        messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": user_msg})

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    reply = response["message"]["content"]

    save_memory("user", user_msg)
    save_memory("assistant", reply)

    return reply
