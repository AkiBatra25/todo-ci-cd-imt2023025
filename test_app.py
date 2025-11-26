# test_app.py
from app import add_task, list_tasks, remove_task, tasks


def setup_function():
    # clear list before each test
    tasks.clear()


def test_add_task():
    msg = add_task("Finish SE lab")
    assert len(tasks) == 1
    assert tasks[0] == "Finish SE lab"
    assert msg == "Task added: Finish SE lab"


def test_add_empty_task():
    msg = add_task("   ")
    assert len(tasks) == 0
    assert msg == "Task cannot be empty."


def test_list_empty():
    assert list_tasks() == "No tasks available."


def test_list_nonempty():
    add_task("First")
    add_task("Second")
    out = list_tasks()
    assert "1. First" in out
    assert "2. Second" in out


def test_remove_valid():
    add_task("First")
    add_task("Second")
    msg = remove_task(1)
    assert len(tasks) == 1
    assert tasks[0] == "Second"
    assert msg == "Task removed: First"


def test_remove_invalid():
    add_task("Only task")
    msg = remove_task(5)
    assert len(tasks) == 1
    assert msg == "Invalid task number."
