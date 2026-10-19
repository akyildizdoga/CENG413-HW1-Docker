
"""CENG413 HW1 - Student Task Manager.

A small Flask application demonstrating Docker containerization,
HTTP endpoints, and environment-based configuration.
"""

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

APP_GREETING = os.environ.get("APP_GREETING", "Hello")
APP_ENV = os.environ.get("APP_ENV", "development")
PORT = int(os.environ.get("PORT", "8080"))

TASKS = [
    {"id": 1, "title": "Complete Docker homework", "completed": False},
    {"id": 2, "title": "Review lecture notes", "completed": True},
    {"id": 3, "title": "Prepare for the exam", "completed": False},
]


@app.get("/")
def home():
    return jsonify(
        application="Student Task Manager",
        environment=APP_ENV,
        message="Welcome to CENG413 HW1",
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/tasks")
def get_tasks():
    return jsonify(tasks=TASKS, total=len(TASKS))


@app.get("/greet")
def greet():
    name = request.args.get("name", "Student")
    return jsonify(message=f"{APP_GREETING}, {name}!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
