from fastapi import FastAPI, UploadFile, File
from app.models import URLRequest, PDFRequest, ChatRequest, ChatResponse
from app.scraping import scrape_url
from app.pdf_processing import extract_text_from_pdf
from app.chat import store_chat_content, get_relevant_response
from app.database import generate_chat_id

app = FastAPI()

@app.post("/process_url")
async def process_url(request: URLRequest):
    content = scrape_url(request.url)
    chat_id = generate_chat_id()
    store_chat_content(chat_id, content)
    return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}

@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    chat_id = generate_chat_id()
    store_chat_content(chat_id, text)
    return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = get_relevant_response(request.chat_id, request.question)
    return {"response": response_text}
