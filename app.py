from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyDbbtUHH05OX9yVQKxaj7Iv3TG_LDe8QzI"

@app.route("/")
def home():
    return "AI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    ai_reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run()
