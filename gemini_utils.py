# gemini_utils.py

from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get the API key from the environment
API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Raise an error if API key is missing
if not API_KEY:
    raise RuntimeError("Please set GEMINI_API_KEY environment variable")

# ✅ Configure the Gemini API
genai.configure(api_key=API_KEY)

# ✅ Initialize the model directly — no need to check methods unless dynamically choosing model
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Function to reformat code using the Gemini model
def reformat_code_with_gemini(prompt: str, code: str) -> str:
    full_prompt = f"{prompt.strip()}\n\n{code.strip()}"
    response = model.generate_content(full_prompt)
    return response.text
