from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "HEAD"],
    allow_headers=["Content-Type"],
)

MODEL = "granite4.1:3b"

# Each message in the conversation history
class Message(BaseModel):
    role: str       # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/generate")
async def generate(body: ChatRequest):
    messages = [{"role": m.role, "content": m.content} for m in body.messages]
    response = ollama.chat(model=MODEL, messages=messages)
    return {"result": response["message"]["content"]}

@app.post("/generate/stream")
async def generate_stream(body: ChatRequest):
    messages = [{"role": m.role, "content": m.content} for m in body.messages]

    def token_stream():
        for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
            content = chunk["message"]["content"]
            if content:
                yield content

    return StreamingResponse(token_stream(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)