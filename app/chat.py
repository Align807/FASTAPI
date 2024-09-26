from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample storage for chat content
chat_storage = {}

def store_chat_content(chat_id: str, content: str):
    chat_storage[chat_id] = content

def get_relevant_response(chat_id: str, question: str) -> str:
    content = chat_storage.get(chat_id)
    if not content:
        return "No content found for the given chat_id."
    
    embeddings = model.encode([content, question])
    cosine_scores = util.cos_sim(embeddings[0], embeddings[1])
    
    return f"The most relevant response is: {content}"  # Simplified for example
