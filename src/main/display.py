def display():
    print("Welcome to To-Do-List")
    print("You have X tasks todo and Y tasks are done!")
    print("Pick an option:")
    print("(1) Show Task List (by date or project)")
    print("(2) Add New Task")
    print("(3) Edit Task (update, mark as done, remove)")
    print("(4) Save and Quit")
    option = input()
    try:
        option = int(option)
        if option == 1:
            print()
        elif option == 2:
            print()
        elif option == 3:
            print()
        elif option == 4:
            print()
        else:
            print("You have entered a wrong option. Try again!")
            display()
    except TypeError:
        print("A number is expected as an option.")
    except ValueError:
        print("Could not convert option to an integer.")
    except:
        print("Unexpected error")


if __name__ == '__main__':
    display()