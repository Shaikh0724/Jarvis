import main  # Jarvis logic
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', template_folder="static")  # Static folder set karo
CORS(app)

@app.route("/")
def serve_frontend():
    # static_folder/index.html serve karega
    return app.send_static_file("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_command = data.get("command", "")
    response = main.processCommand(user_command)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

























 







































