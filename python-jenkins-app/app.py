from flask import Flask, render_template, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()

    return render_template(
        "index.html",
        hostname=hostname,
        environment=os.getenv("APP_ENV", "Development")
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Python Jenkins Deployment App"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000"))
    )