
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Backend is running successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    # Simple AI logic (Version 1)
    if "hello" in user_message.lower():
        reply = "Hello 👋 I am your AI assistant!"
    elif "how are you" in user_message.lower():
        reply = "I'm just code, but I'm running perfectly!"
    else:
        reply = "You said: " + user_message

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
