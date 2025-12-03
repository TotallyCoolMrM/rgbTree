from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/on")
def lights_on():
    subprocess.Popen([
        "sudo",
        "/home/administrator/venv/bin/python3",
        "/home/administrator/rgbTree/programs/codeFiles/main.py"
    ])
    return jsonify({"ran": "main.py"})

@app.route("/off")
def lights_off():
    subprocess.Popen([
        "sudo",
        "/home/administrator/venv/bin/python3",
        "/home/administrator/tree/programs/codeFiles/off.py"
    ])
    return jsonify({"ran": "off.py"})

@app.route("/")
def home():
    return jsonify({"status": "ready"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
