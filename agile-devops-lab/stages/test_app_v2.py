"""Tests for the Task Manager API."""
import pytest

from src.app import app, reset_state


@pytest.fixture
def client():
    reset_state()
    app.config["TESTING"] = True
    return app.test_client()


def make_task(client, title="Write report"):
    return client.post("/tasks", json={"title": title}).get_json()


# ---------- US1: create a task ----------
def test_create_task_returns_201_and_open_status(client):
    r = client.post("/tasks", json={"title": "Study DevOps"})
    assert r.status_code == 201
    body = r.get_json()
    assert body["id"] == 1
    assert body["title"] == "Study DevOps"
    assert body["status"] == "open"


def test_create_task_ids_increment(client):
    assert make_task(client, "A")["id"] == 1
    assert make_task(client, "B")["id"] == 2


def test_create_task_trims_whitespace(client):
    r = client.post("/tasks", json={"title": "  padded  "})
    assert r.get_json()["title"] == "padded"


def test_create_task_empty_title_returns_400(client):
    r = client.post("/tasks", json={"title": "   "})
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_create_task_missing_title_returns_400(client):
    assert client.post("/tasks", json={}).status_code == 400


def test_create_task_no_body_returns_400(client):
    assert client.post("/tasks").status_code == 400


def test_create_task_non_string_title_returns_400(client):
    assert client.post("/tasks", json={"title": 123}).status_code == 400


# ---------- US2: list tasks ----------
def test_list_tasks_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []


def test_list_tasks_returns_all_created(client):
    make_task(client, "A")
    make_task(client, "B")
    titles = [t["title"] for t in client.get("/tasks").get_json()]
    assert titles == ["A", "B"]
