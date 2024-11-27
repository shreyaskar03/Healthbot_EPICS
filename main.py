from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import google.generativeai as genai

# Load the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

if GOOGLE_API_KEY:
    print("API key is configured.")

# Chat settings
generation_config = {
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = """
You are MindMate, a mental health chatbot designed to provide empathetic support and general mental health advice. 
Your goal is to engage users in meaningful conversations, make them feel valued, and encourage positivity. 
When needed, suggest seeing a mental health professional for further assistance.
Avoid providing diagnostic or medical advice and focus on emotional support.
"""

# FastAPI application
app = FastAPI()

# Allow CORS for frontend integration
origins = [
    "https://your-frontend-url.com",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and response model
class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def get_response(user_message: UserMessage):
    try:
        user_input = user_message.message
        
        # Generate a response
        response = genai.chat(
            messages=[{"role": "system", "content": system_instruction},
                      {"role": "user", "content": user_input}],
            **generation_config
        )
        
        return {"response": response['candidates'][0]['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/chat_history")
async def fetch_chat_history():
    try:
        # This feature can be customized further as needed
        return {"message": "Chat history functionality is not implemented yet."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
