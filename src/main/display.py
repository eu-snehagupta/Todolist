from todolist import Todolist

to_do_list = Todolist()


def display():
    display_welcome_message()
    display_option_details()
    user_choice = input()
    handle_choice(user_choice)


def display_welcome_message():
    print("***********************************")
    print("Welcome to To-Do-List")
    print("You have X tasks todo and Y tasks are done!")


def display_option_details():
    print("Pick an option:")
    print("(1) Show Task List (by date or project)")
    print("(2) Add New Task")
    print("(3) Edit Task (update, mark as done, remove)")
    print("(4) Save and Quit")


def handle_choice(choice):
    try:
        choice = int(choice)
        select(choice)
    except ValueError:
        print("Invalid Input. Expecting an integer!" + "\nTry again!")
        return display()


def select(choice):
    if choice == 1:
        to_do_list.print_list()
        input("Enter any key to continue-->")
        return display()
    elif choice == 2:
        to_do_list.add_task_to_list()
        input("Enter any key to continue-->")
        return display()
    elif choice == 3:
        print("choice3")
        input("Enter any key to continue-->")
        return display()
    elif choice == 4:
        to_do_list.save_quit()
        print("File Saved! \nTack. Enjoy the day.")
        return
    else:
        print("Invalid choice!" + "\nTry again!")


if __name__ == '__main__':
    display()