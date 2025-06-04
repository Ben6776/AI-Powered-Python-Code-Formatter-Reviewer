# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gemini_utils import reformat_code_with_gemini

app = FastAPI()

class CodeInput(BaseModel):
    code: str
    prompt: str

@app.post("/reformat-code")
def reformat_code(data: CodeInput):
    try:
        suggestions = reformat_code_with_gemini(data.prompt, data.code)
        return {
            "output": data.code,
            "suggestions": suggestions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
