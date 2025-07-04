import streamlit as st
import requests

API_URL = "http://localhost:8000/reformat-code"

st.set_page_config(page_title="Python Code Formatter Bot", layout="wide")

st.title(" Upload Python File for AI Review")
st.markdown("Upload a `.py` file and get custom AI feedback using your own prompt.")

uploaded_file = st.file_uploader("Choose a Python file", type=["py"])

user_prompt = ("Please analyze the uploaded Python file and return a version of the code that follows standard Python coding practices (PEP 8), improves readability, and fixes any common style or formatting issues. Do not change the logic of the code.")

if uploaded_file is not None and user_prompt:
    file_code = uploaded_file.read().decode("utf-8")

    if st.button("🤖Format Code"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"code": file_code, "prompt": user_prompt},
                    timeout=100
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ AI Response Received")
                    st.subheader("📄 Original Code:")
                    st.code(data["output"], language="python")
                    
                    st.subheader("💡 AI Suggestions / Output:")
                    st.write(data["suggestions"])
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Connection error: {e}")
