"""Task Manager API - a tiny Flask service for tracking tasks."""
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
_state = {"next_id": 1}


def reset_state():
    """Clear all tasks and restart ID numbering (used by the tests)."""
    tasks.clear()
    _state["next_id"] = 1


@app.post("/tasks")
def create_task():
    """US1 - create a task. Requires a non-empty string title."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = {}
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify(error="title is required"), 400
    task = {"id": _state["next_id"], "title": title.strip(), "status": "open"}
    tasks.append(task)
    _state["next_id"] += 1
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
