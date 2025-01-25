from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Define a model for the query request
class QueryRequest(BaseModel):
    query: str

# MySQL Database connection (adjust credentials)
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_user",  # Change to your DB user
        password="your_password",  # Change to your DB password
        database="your_db"  # Change to your DB name
    )
    return conn

# Fetch data from the database based on the query
def fetch_data(query: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{query}%'")  # Example query
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API"}

@app.post("/query")
async def handle_query(request: QueryRequest):
    try:
        # Get the query from the frontend
        query = request.query
        if not query:
            return {"error": "No query provided"}

        # Fetch data from the database
        data = fetch_data(query)

        # Return response
        return {"answer": data}

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}
