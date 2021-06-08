from datetime import datetime
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
            print_statements("The list is empty!")
        else:
            for element in todolist:
                print(element.title, element.due_date, element.status, element.project)

    def add_task_to_list(self):
        new_task = self.get_task_details_from_user()
        self.add_to_list(new_task)
        print_statements("Task added successfully!")
        return self.todolist

    def get_task_details_from_user(self):
        task_title = input("Enter the task title: ")

        task_due_date = input("Enter the task due date(dd/mm/yy): ")
        try:
            task_due_date = datetime.strptime(task_due_date, '%d/%m/%y')
        except:
            print_statements("Incorrect due date format.")
            exit(0)

        task_status = input("Enter the task status (1) Done, (2) Undone: ")
        try:
            task_status = int(task_status)
            if task_status == 1:
                task_status = "Done"
            elif task_status == 2:
                task_status = "Undone"
            else:
                print_statements("Incorrect choice")
        except ValueError:
            print_statements("Invalid Input. Expecting an integer!")
            exit(0)

        task_project = input("Enter the task project: ")

        task = Task(task_title, task_due_date, task_status, task_project)
        return task

    def save_quit(self):
        file_handler.write_as_data(self.todolist)


def print_statements(statements):
    print(statements)
