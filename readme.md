
````markdown
# 📝 Task CLI – Simple Command-Line Task Manager

A lightweight and pure Python command-line tool to manage your tasks easily — without any external libraries. for https://roadmap.sh/projects/task-tracker

## 📦 Features

- ✅ Add new tasks  
- ✏️ Update task titles  
- ❌ Delete tasks  
- 🔁 Mark tasks as `todo`, `in-progress`, or `done`  
- 📋 List all tasks or filter them by status  
- 💾 All data is stored in a local `tasks.json` file

---

## ⚙️ Installation

Just clone the repo or copy the `task-cli.py` file to your desired folder:

```bash
git clone https://github.com/your-username/task-cli.git
cd task-cli
````

> Make sure you have **Python 3.x** installed.

---

## 🚀 Usage

### 🆕 Add a task

```bash
python task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### ✏️ Update a task

```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
```

### ❌ Delete a task

```bash
python task-cli.py delete 1
```

### 🔁 Mark a task as in-progress or done

```bash
python task-cli.py mark-in-progress 1
python task-cli.py mark-done 1
```

### 📋 List tasks

List all tasks:

```bash
python task-cli.py list
```

List tasks by status:

```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

---

## ❓ Help

```bash
python task-cli.py
```

This will show you a full list of available commands and usage.

---

## 🪟 Windows Support

If you want to use `task-cli` like a native command in Windows, create a `task-cli.bat` file:

```bat
@echo off
python path\to\task-cli.py %*
```

Then add the `.bat` file’s folder to your system PATH so you can run:

```bash
task-cli add "Do something"
```

---

## 📁 Data Format

All your tasks are stored in `tasks.json` in the current directory. Example:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Buy groceries",
      "status": "todo"
    }
  ]
}
```

---

## 🧠 License

Free to use for educational and personal projects ✌️


---

```



