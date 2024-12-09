



'''
@author: Soundarya

source:
    ?
'''


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/reverse")
async def reverse_text(input: TextInput):
    reversed_text = input.text[::-1]
    return {
        "original_text": input.text,
        "reversed_text": reversed_text
        }

@app.get("/")
async def root():
    return {
        "message": "Send a POST request to /reverse with a 'text' field to reverse it.
        "}
