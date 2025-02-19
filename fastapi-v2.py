import streamlit as st

st.title("How to Build an API with FastAPI")

st.header("Requirements")
st.write("- Install FastAPI and Uvicorn using `pip install fastapi uvicorn`.")

st.header("Setup")
st.write("1. Create a Python script with an instance of FastAPI (`app`).")
st.write("2. Define an `Item` class as a base model for item objects.")
st.write("3. Create a dictionary of sample items for testing.")

st.header("Endpoints")
st.write("- `GET /index`: Returns all items as JSON data.")
st.write("- `GET /items/{item_id}`: Returns an item by its ID.")
st.write("- `GET /items`: Returns items based on query parameters (e.g., name, price).")
st.write("- `POST /items`: Adds a new item to the dictionary.")
st.write("- `PUT /items/{item_id}`: Updates an existing item by its ID.")
st.write("- `DELETE /items/{item_id}`: Deletes an item by its ID.")

st.header("Key Features of FastAPI")
st.write("- Automatic JSON serialization/deserialization.")
st.write("- Type-hinted arguments and results ensure data validation.")
st.write("- Built-in documentation generation using docstrings.")
st.write("- Support for additional constraints using `Path` and `Query` from FastAPI.")

st.header("Tips for Validation")
st.write("- Use path and query parameters to enforce additional constraints.")
st.write("- Define responses for specific status codes to provide clear error messages.")

st.header("Scalability Considerations")
st.write("- FastAPI's scalability is influenced by Python's concurrency limitations.")
st.write("- Consider using Gunicorn instead of Uvicorn for improved worker process management.")
st.write("- Implement load balancing in your cloud architecture.")

st.header("Alternative to REST")
st.write("- GraphQL offers a different approach to API development.")
st.write("- Consider GraphQL if you need more flexibility in querying your API.")

if __name__ == "__main__":
    st.write("FastAPI guide application is running.")
