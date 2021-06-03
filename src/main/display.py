import todolist
import task


def get_task_details():
    task_title = input("Enter the task title: ")
    task_due_date = input("Enter the task due date: ")
    task_status = input("Enter the task status (1) Done, (2) Undone: ")
    task_project = input("Enter the task project: ")
    return task_title, task_due_date, task_status, task_project


def switch(choice):
    to_do_list = todolist.Todolist
    if choice == 1:
        print(to_do_list.get_list())
        handle_option()
    elif choice == 2:
        a,b,c,d = get_task_details()
        new_task = task.Task(a,b,c,d)
        print(new_task)
        to_do_list.add_to_list(new_task)
        handle_option()
    elif choice == 3:
        print()
        handle_option()
    elif choice == 4:
        print()
        return
    else:
        print("You have entered a wrong option. Try again!")


def display_welcome_message():
    print("Welcome to To-Do-List")
    print("You have X tasks todo and Y tasks are done!")


def display_option_details():
    print("Pick an option:")
    print("(1) Show Task List (by date or project)")
    print("(2) Add New Task")
    print("(3) Edit Task (update, mark as done, remove)")
    print("(4) Save and Quit")


def handle_option():
    display_option_details()
    option = input()
    try:
        option = int(option)
        switch(option)
    except ValueError:
        print("Could not convert option to an integer.")


if __name__ == '__main__':
    display_welcome_message()
    handle_option()