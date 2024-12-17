import streamlit as st

# Configure the Streamlit page
st.set_page_config(page_title="Complete FastAPI Guide", layout="wide")
st.title("🚀 Complete FastAPI Guide: From Basics to Advanced")

st.markdown("""
Welcome to the **Complete FastAPI Guide**. This app is your one-stop resource for learning and mastering FastAPI. 
It covers everything from basic examples to advanced features, deployment, testing, and best practices.
""")

# Section: Introduction to FastAPI
st.subheader("📘 Introduction to FastAPI")
st.markdown("""
FastAPI is a modern framework for building APIs with Python. It is:
- **Fast**: Built on ASGI and optimized for speed.
- **Easy to use**: Leverages Python type hints for request/response validation.
- **Automatically documented**: Generates OpenAPI and Swagger docs.
- **Production-ready**: Used by major companies like Netflix, Microsoft, and Uber.

**Why choose FastAPI?**
- It is one of the fastest frameworks available.
- It integrates seamlessly with tools like Pydantic and Starlette.
- It supports asynchronous programming, making it ideal for high-performance apps.
""")

st.info("💡 Tip: FastAPI's documentation is automatically generated using the OpenAPI standard, available at `/docs` or `/redoc`.")

# Section: Basic Example
st.subheader("📂 Basic FastAPI Example")
st.markdown("""
Here's an example of a simple FastAPI app with two endpoints:
""")
st.code("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
""", language="python")

st.markdown("""
To run this app, save it as `main.py` and run:
```bash
uvicorn main:app --reload
