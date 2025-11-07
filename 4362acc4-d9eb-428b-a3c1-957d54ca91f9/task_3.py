class TaskManager:
    def __init__(self):
        self.__tasks = {}
        self._counter = 0

    def __len__(self):
        return len(self.__tasks)

    def __getitem__(self, key):
        return self.__tasks[key]

    def __setitem__(self, key, value):
        if not isinstance(value, dict) or 'priority' not in value or 'description' not in value:
            raise ValueError("Завдання повинно містити 'priority' та 'description'")
        self.__tasks[key] = value

    def __iter__(self):
        return iter(sorted(self.__tasks.items(), key=lambda x: x[1]['priority'], reverse=True))

    def __contains__(self, key):
        return key in self.__tasks

    def add_task(self, description, priority):
        self._counter += 1
        self[self._counter] = {'description': description, 'priority': priority}
        return self._counter

    def __str__(self):
        return f"Task id is {self._counter}"



# TaskManager
tm = TaskManager()
print('TM is: ', tm)
task1_id = tm.add_task("Написати звіт", 3)
task2_id = tm.add_task("Зустріч з клієнтом", 1)
task3_id = tm.add_task("Перевірити пошту", 2)

print("\nВсі завдання в порядку пріоритету:")

for task_id, task in tm:
    print(f"ID: {task_id}, Пріоритет: {task['priority']}, Опис: {task['description']}")

# print(task1_id + 5555)
