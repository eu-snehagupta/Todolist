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
                print(i, " : " +task_list[i].title, task_list[i].due_date, task_list[i].status, task_list[i].project)

    def add_task(self):
        new_task = self.get_task_details_from_user()
        self.add_to_list(new_task)
        print_statements("Task added successfully!")
        return self.todolist

    def edit_task(self, choice):
        try:
            choice = int(choice)
            self.select_edit_choice(choice)
        except ValueError:  # handling situation where user input a choice other than an integer
            print_statements("Invalid Input. Expecting an integer!" + "\nTry again!")

    def select_edit_choice(self, choice):
        if choice == 1:
            self.update_task()
        elif choice == 2:
            self.mark_as_done()
        elif choice == 3:
            self.remove_task()
        else:
            print_statements("Invalid choice!" + "\nTry again!")   # handling the situation where user input
                                                              # a choice other than the choice available
    def update_task(self):
        self.show_list()
        pass

    def mark_as_done(self):
        pass

    def remove_task(self):
        self.show_list()
        pass

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
