from typing import Union

from fastapi import FastAPI

from google import genai

app = FastAPI()

client = genai.Client(api_key="AIzaSyD_bfFpqh_wlT1GmroI0xS7kzQS3XV5Y3k")


@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/test")
def test():
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="너 이름이 뭐니?"
    )
    return {"response": response.text}