import file_handler
from task import Task


class Todolist:

    def __init__(self):
        self.todolist = file_handler.read_as_data()

    def get_list(self):
        return self.todolist

    def add_to_list(self, task):
        self.todolist.append(task)
        return self.todolist

    def update_list(self, old_task, update_task):
        index = self.todolist.index(old_task)
        self.todolist[index] = update_task
        return self.todolist

    def remove_list(self):
        del self.todolist

    def remove_task_from_list(self, task):
        self.todolist.remove(task)

    def print_list(self):
        todolist = self.get_list()
        if len(todolist) == 0:
            print("The list is empty!")
        else:
            for element in todolist:
                print(element.title, element.due_date, element.status, element.project)

    def add_task_to_list(self):
        task_title = input("Enter the task title: ")
        task_due_date = input("Enter the task due date: ")
        task_status = input("Enter the task status (1) Done, (2) Undone: ")
        task_project = input("Enter the task project: ")

        task = Task(task_title, task_due_date, task_status, task_project)
        self.add_to_list(task)
        print("Task added successfully!")
        return self.todolist

    def save_quit(self):
        file_handler.write_as_data(self.todolist)
