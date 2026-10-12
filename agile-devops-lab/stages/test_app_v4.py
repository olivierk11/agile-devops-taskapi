"""Tests for the Task Manager API."""
import logging

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


# ---------- US3: complete a task ----------
def test_complete_task_sets_status_done(client):
    task = make_task(client)
    r = client.patch(f"/tasks/{task['id']}/complete")
    assert r.status_code == 200
    assert r.get_json()["status"] == "done"


def test_complete_task_persists_in_list(client):
    task = make_task(client)
    client.patch(f"/tasks/{task['id']}/complete")
    assert client.get("/tasks").get_json()[0]["status"] == "done"


def test_complete_unknown_task_returns_404(client):
    assert client.patch("/tasks/999/complete").status_code == 404


# ---------- US7: health, logging, error handling ----------
def test_health_returns_ok(client):
    r = client.get("/health")
    assert r.status_code == 200
    body = r.get_json()
    assert body["status"] == "ok"
    assert "uptime_seconds" in body


def test_health_reports_task_count(client):
    make_task(client)
    make_task(client)
    assert client.get("/health").get_json()["tasks"] == 2


def test_requests_are_logged(client, caplog):
    with caplog.at_level(logging.INFO, logger="taskapi"):
        client.get("/health")
    assert any("GET /health -> 200" in m for m in caplog.messages)


def test_unknown_route_returns_json_404(client):
    r = client.get("/nope")
    assert r.status_code == 404
    assert "error" in r.get_json()


def test_unhandled_exception_returns_json_500(client, monkeypatch):
    def boom():
        raise RuntimeError("simulated failure")

    monkeypatch.setitem(app.view_functions, "health", boom)
    r = client.get("/health")
    assert r.status_code == 500
    assert r.get_json() == {"error": "internal server error"}
