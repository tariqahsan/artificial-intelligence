# from fastapi import FastAPI
# from pydantic import BaseModel
# from openai import OpenAI

# app = FastAPI()  # Make sure this is at the top of the file

# # Set your API key here or use an environment variable
# OPENAI_API_KEY = "your openai secret api key"

# client = OpenAI(api_key=OPENAI_API_KEY)

# # Define request body structure
# class ChatRequest(BaseModel):
#     message: str

# @app.post("/chat")
# async def chat_endpoint(request: ChatRequest):
#     try:
#         completion = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": request.message}]
#         )
#         return {"response": completion.choices[0].message.content}
#     except Exception as e:
#         return {"error": str(e)}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your openai secret api key")
client = OpenAI(api_key=OPENAI_API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

