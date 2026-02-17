from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get API key from environment variable (we will set this in Render)
API_KEY = os.environ.get("GENIE_API_KEY")

# Google Gemini REST API endpoint
GENIE_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

@app.route("/")
def home():
    return "AI Backend is running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": question}
                    ]
                }
            ]
        }

        response = requests.post(
            f"{GENIE_API_URL}?key={API_KEY}",
            headers=headers,
            json=payload
        )

        result = response.json()

        answer = result["candidates"][0]["content"]["parts"][0]["text"]

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
