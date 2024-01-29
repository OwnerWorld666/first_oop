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

if __name__ == "__main__":
    json_filename = input("Введите имя файла для сохранения/загрузки данных: ")
    task_manager = TaskManager(json_filename)

    while True:
        print("\nВыберите действие:")
        print("1. Создать задачу")
        print("2. Просмотреть список задач")
        print("3. Изменить статус задачи")
        print("4. Посмотреть информацию о конкретной задаче")
        print("5. Посмтреть историю действий")
        print("6. Выйти и очистить json файл")

        choice = input("Введите номер действия: ")
        if choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            task_manager.create_task(title, description)
            print("Задача создана!")

        elif choice == "2":
            tasks = task_manager.view_all_tasks()
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.title} - {task.status}")


        elif choice == "3":
            tasks = task_manager.view_all_tasks()
            if not tasks:
                print("Пока нет задач. Создайте свою первую задачу.")

            else:
                while True:
                    task_index = int(input("Введите номер задачи: ")) - 1
                    if 0 <= task_index < len(tasks):
                        new_status = input("Введите новый статус (new - новая, in_progress - выполняется, "
                                           "review - просматривается, completed - завершена, canceled - отменена): ")

                        task = task_manager.select_task(task_index)
                        if new_status.lower() == "canceled":
                            del task_manager.tasks[task_index]
                            print(f"Задача {task.title} удалена.")
                            for i in range(task_index, len(task_manager.tasks)):
                                task_manager.tasks[i].title = f"Задача {i + 1}"
                            break
                        else:
                            task_manager.change_task_status(task, TaskStatus[new_status.lower()])
                            print(f"Статус {task.title} изменен на {new_status}")
                            break
                    else:
                        print("Задачи с таким номером нет. Попробуйте еще раз.")

        elif choice == "4":
            tasks = task_manager.view_all_tasks()

            if not tasks:
                print("Пока нет задач. Создайте свою первую задачу.")

            else:
                while True:
                    task_index = int(input("Введите номер задачи: ")) - 1
                    if 0 <= task_index < len(tasks):
                        task = task_manager.select_task(task_index)
                        print("\nИнформация о задаче:")
                        print(f"Название: {task.title}")
                        print(f"Описание: {task.description}")
                        print(f"Статус: {task.status}")
                        print(f"Дата создания: {task.creation_date}")
                        print(f"Дата последнего просмотра: {task.last_viewed_date}")
                        break
                    else:
                        print("Задачи с таким номером нет. Попробуйте еще раз.")

        elif choice == "5":
            task_manager.view_action_history()

        elif choice == "6":
            print("КОНЕЦ")
            task_manager.clear_json_file()
            break

        else:
            print("Неверный ввод. Попробуйте еще раз.")


#C:\Users\vladi\AppData\Roaming\JetBrains\PyCharmCE2023.1\light-edit\JSON.json
