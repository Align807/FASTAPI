from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample storage for chat content
chat_storage = {}

def store_chat_content(chat_id: str, content: str):
    chat_storage[chat_id] = content

'''
def get_relevant_response(chat_id: str, question: str) -> str:
    content = chat_storage.get(chat_id)
    if not content:
        return "No content found for the given chat_id."
    
    embeddings = model.encode([content, question])
    cosine_scores = util.cos_sim(embeddings[0], embeddings[1])
    
    return f"The most relevant response is: {content}"  # Simplified for example
'''
#def get_relevant_response(content: str, question: str) -> str:

def get_relevant_response(chat_id: str, question: str) -> str:
    # Split content into sentences
    content = chat_storage.get(chat_id)
    if not content:
        return "No content found for the given chat_id."
    content_sentences = content.split(". ")
    
    # Encode all sentences and the question
    content_embeddings = model.encode(content_sentences, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)
    
    # Compute cosine similarity between question and content sentences
    similarity_scores = util.pytorch_cos_sim(question_embedding, content_embeddings)[0]
    
    # Get the index of the most similar sentence
    best_idx = similarity_scores.argmax().item()
    
    # Return the most relevant sentence
    return f"The most relevant response is: {content_sentences[best_idx]}"