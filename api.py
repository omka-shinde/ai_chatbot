# api.py
from flask import Flask, request, jsonify
from app import chatbot_query  # Import the chatbot query function from app.py

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's query from the incoming JSON body
    user_query = request.json.get('query')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Call the chatbot query function from app.py
    response = chatbot_query(user_query)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
