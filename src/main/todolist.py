from datetime import datetime
import file_handler
from task import Task


class Todolist:
    #############################################CRUD.METHODS##################################################################
    def __init__(self):
        self.todolist = file_handler.read_as_data()         # updates the list from the resources/Todolist.txt file

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

    ################################################USER.METHODS###############################################################
    def show_list(self):
        task_list = self.get_list()
        if len(task_list) == 0:
            print_statements("The list is empty!")
        else:
            for i in range(len(task_list)):
                print(i+1, " : " + task_list[i].title, task_list[i].due_date, task_list[i].status, task_list[i].project)

    def add_task(self):
        new_task = self.get_task_details_from_user()
        self.add_to_list(new_task)
        print_statements("Task added successfully!")
        return self.todolist

    def update_task(self):
        task_list = self.get_list()
        self.show_list()
        task_index = self.select_task_to_be_edited()
        old_task = task_list[task_index]
        new_task = self.get_task_details_from_user()
        self.update_list(old_task, new_task)
        print_statements("Task updated successfully!")
        return self.todolist


    def mark_as_done(self):
        task_list = self.get_list()
        self.show_list()
        task_index = self.select_task_to_be_edited()
        task_to_mark_as_done = task_list[task_index]
        if task_to_mark_as_done.status == "Done":
            print_statements("Task is already under status done!")
        else:
            task_to_mark_as_done.status = "Done"
            print_statements("Task updated as done successfully!")
        return self.todolist

    def remove_task(self):
        task_list = self.get_list()
        self.show_list()
        task_index = self.select_task_to_be_edited()
        task_to_remove = task_list[task_index]
        self.remove_task_from_list(task_to_remove)
        print_statements("Task removed successfully!")
        return self.todolist

    def select_task_to_be_edited(self):
        task_number = input("Enter the task number to be edited: ")
        try:
            task_number = int(task_number)
            return self.fetch_task(task_number)
        except ValueError:  # handling situation where user input a choice other than an integer
            print_statements("Invalid Input. Expecting an integer!" + "\nTry again!")
            return self.select_task_to_be_edited()

    def fetch_task(self, index):
        task_list = self.get_list()
        if 0 < index < len(task_list)+1:
            return index - 1
        else:
            print_statements("Invalid choice!" + "\nTry again!")  # handling the situation where user input
            return self.select_task_to_be_edited()                              # a choice other than the choice available

    def get_task_details_from_user(self):
        task_title = self.get_task_title_from_user()
        task_due_date = self.get_task_due_date_from_user()
        task_status = self.get_task_status_from_user()
        task_project = self.get_task_project_from_user()
        task = Task(task_title, task_due_date, task_status, task_project)
        return task

    def get_task_title_from_user(self):
        return input("Enter the task title: ")

    def get_task_due_date_from_user(self):
        task_due_date = input("Enter the task due date(dd/mm/yyyy): ")
        try:
            task_due_date = datetime.strptime(task_due_date, "%d/%m/%Y").date()
            return task_due_date                # accepts the dates in the dd/mm/yyyy and
                                                # saves it as yyyy-mm-dd
        except ValueError:
            print_statements("Incorrect due date format.\n Try Again!")
            return self.get_task_due_date_from_user()

    def get_task_status_from_user(self):
        task_status = input("Enter the task status (1) Done, (2) Undone: ")
        try:
            task_status = int(task_status)
            if task_status == 1:
                return "Done"
            elif task_status == 2:
                return "Undone"
            else:
                print_statements("Invalid choice!" + "\nTry again!")    # handling the situation where user input
                return self.get_task_status_from_user()                 # a choice other than the choice available
        except ValueError:
            print_statements("Invalid Input. Expecting an integer! \n Try Again!")
            return self.get_task_status_from_user()          # handling situation where user input a
                                                                # choice other than an integer

    def get_task_project_from_user(self):
        return input("Enter the task project: ")


    def save_quit(self):
        file_handler.write_as_data(self.todolist)


def print_statements(statements):
    print(statements)
