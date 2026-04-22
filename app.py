from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome! AI Service is running successfully 🚀"
    })


@app.route("/health")
def health_check():
    return jsonify({
        "status": "OK",
        "service": "AI Backend",
        "message": "Service is healthy and running"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)