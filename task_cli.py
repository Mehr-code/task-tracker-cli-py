import json
import os
import sys

TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump({"tasks": []}, f)
    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_task(title):
    data = load_tasks()
    tasks = data["tasks"]
    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    tasks.append({"id": new_id, "title": title, "status": "todo"})
    save_tasks(data)
    print(f"Task added successfully (ID: {new_id})")


def update_task(task_id, new_title):
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["title"] = new_title
            save_tasks(data)
            print("Task updated.")
            return
    print("Task not found.")


def delete_task(task_id):
    data = load_tasks()
    tasks = data["tasks"]
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print("Task not found.")
    else:
        data["tasks"] = new_tasks
        save_tasks(data)
        print("Task deleted.")


def mark_status(task_id, status):
    if status not in ["todo", "in-progress", "done"]:
        print("Invalid status.")
        return
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(data)
            print(f"Task marked as {status}.")
            return
    print("Task not found.")


def list_tasks(filter_status=None):
    data = load_tasks()
    tasks = data["tasks"]
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - {task['status']}")


def show_help():
    print(
        """
Usage:
  task-cli.py add "Task title"
  task-cli.py update <id> "New title"
  task-cli.py delete <id>
  task-cli.py mark-done <id>
  task-cli.py mark-in-progress <id>
  task-cli.py list
  task-cli.py list <status>  # todo | in-progress | done
"""
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "update":
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "mark-done":
        mark_status(int(sys.argv[2]), "done")
    elif command == "mark-in-progress":
        mark_status(int(sys.argv[2]), "in-progress")
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        show_help()
