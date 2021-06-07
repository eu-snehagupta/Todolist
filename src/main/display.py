#
# def get_task_details():
#     task_title = input("Enter the task title: ")
#     task_due_date = input("Enter the task due date: ")
#     task_status = input("Enter the task status (1) Done, (2) Undone: ")
#     task_project = input("Enter the task project: ")
#     return task_title, task_due_date, task_status, task_project

def display():
    display_welcome_message()
    display_option_details()
    input_option = int(input())
    handle_option(input_option)


def display_welcome_message():
    print("Welcome to To-Do-List")
    print("You have X tasks todo and Y tasks are done!")


def display_option_details():
    print("Pick an option:")
    print("(1) Show Task List (by date or project)")
    print("(2) Add New Task")
    print("(3) Edit Task (update, mark as done, remove)")
    print("(4) Save and Quit")


def handle_option(option):
    try:
        switch(option)
    except ValueError:
        print("Could not convert option to an integer.")


def switch(choice):
    if choice == 1:
        print("choice1")
        return display()
    elif choice == 2:
        print("choice2")
        return display()
    elif choice == 3:
        print("choice3")
        return display()
    elif choice == 4:
        print("choice4")
        return
    else:
        print("You have entered a wrong option. Try again!")


if __name__ == '__main__':
    display()