from typing import Union

from fastapi import FastAPI

from google import genai

app = FastAPI()

client = genai.Client(api_key="YOUR_API_KEY")


@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/test")
def test():
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Explain how AI works in a few words"
    )
    return {"response": response.text}