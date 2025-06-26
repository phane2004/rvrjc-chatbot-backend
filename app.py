from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS  # type: ignore
from nlp_model import get_response

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

@app.route("/", methods=["GET"])
def home():
    return "Server is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    bot_reply = get_response(user_input)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
