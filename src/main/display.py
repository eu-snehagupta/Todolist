from todolist import Todolist

to_do_list = Todolist()


def display():
    display_welcome_message()
    display_option_details()
    user_choice = input()
    handle_choice(user_choice)


def display_welcome_message():
    print_statement("***********************************" +
          "\nWelcome to To-Do-List" +
          "\nYou have X tasks todo and Y tasks are done!")


def display_option_details():
    print_statement("Pick an option:" +
          "\n(1) Show Task List (by date or project)" +
          "\n(2) Add New Task" +
          "\n(3) Edit Task (update, mark as done, remove)" +
          "\n(4) Save and Quit")


def handle_choice(choice):
    try:
        choice = int(choice)
        select(choice)
    except ValueError:
        print_statement("Invalid Input. Expecting an integer!" + "\nTry again!")
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
        print_statement("choice3")
        input("Enter any key to continue-->")
        return display()
    elif choice == 4:
        to_do_list.save_quit()
        print_statement("File Saved! \nTack. Enjoy the day.")
        return
    else:
        print_statement("Invalid choice!" + "\nTry again!")


def print_statement(statement):
    print(statement)


if __name__ == '__main__':
    display()