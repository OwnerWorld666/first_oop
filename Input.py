from first_oop import TaskStatus, TaskManager, Task


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
        print("6. Выйти и очистить json файл") #возможно, очищать не имело смысла, но пускай это будет аналог очищения истории браузера)

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

