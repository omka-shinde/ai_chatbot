from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector  # Use psycopg2 for PostgreSQL

app = FastAPI()

# Allow CORS for the frontend (React app running on localhost:3000)
origins = [
    "http://localhost:3000",  # React frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define a model for the query request
class QueryRequest(BaseModel):
    query: str

# MySQL Database connection (you can change this to PostgreSQL if needed)
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="omkar",  # Change this
        password="Biology@2",  # Change this
        database="chatbot_db"  # Change this
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

# Define the route to handle queries from the frontend
@app.post("/query")
async def get_query_response(request: QueryRequest):
    try:
        query = request.query
        data = fetch_data(query)
        return {"response": data}
    except Exception as e:
        return {"error": str(e)}

