from pydantic import BaseModel
from typing import Optional

class URLRequest(BaseModel):
    url: str

class PDFRequest(BaseModel):
    file: bytes

class ChatRequest(BaseModel):
    chat_id: str
    question: str

class ChatResponse(BaseModel):
    response: str
