import json
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    new = "Новая"
    in_progress = "Выполняется"
    review = "Просматривается"
    completed = "Завершена"
    canceled = "Отменена"

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = TaskStatus.new
        self.creation_date = datetime.now()
        self.last_viewed_date = datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.name,
            "creation_date": str(self.creation_date),
            "last_viewed_date": str(self.last_viewed_date) if self.last_viewed_date else None
        }

class TaskManager:
    def __init__(self, json_filename):
        self.tasks = []
        self.json_filename = json_filename

        try:
            self.load_from_json()
            print("Данные успешно загружены из файла.")
        except FileNotFoundError:
            print("Файл не найден. Новый файл будет создан.")

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.save_to_json()
        return task

    def view_all_tasks(self):
        if not self.tasks:
            print("Пока нет задач. Создайте свою первую задачу.")
        else:
            return self.tasks

    def change_task_status(self, task, new_status):
        task.status = new_status
        task.last_viewed_date = datetime.now()
        self.save_to_json()

    def select_task(self, task_index):
        return self.tasks[task_index]

    def save_to_json(self):
        with open(self.json_filename, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file, indent=4)

    def load_from_json(self):
        with open(self.json_filename, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [Task(title=data["title"], description=data["description"]) for data in tasks_data]

    def view_action_history(self):
        if not self.tasks:
            print("Пока нет задач. Создайте свою первую задачу.")
        else:
            for task in self.tasks:
                if task.last_viewed_date:
                    print(f"Задача: {task.title}")
                    print(f"Описание: {task.description}")
                    print(f"Статус: {task.status}")
                    print(f"Дата создания: {task.creation_date}")
                    print(f"Дата последнего просмотра: {task.last_viewed_date}")
                    print("---")

    def clear_json_file(self):
        with open(self.json_filename, 'w') as file:
            json.dump([], file, indent=4)

