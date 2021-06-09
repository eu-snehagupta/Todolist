from task import Task


def read_as_data():
    task_list = []
    try:
        file = open("../resources/Todolist.txt", "r")
        entries = file.readlines()
        for entry in entries:
            data = entry.split("**")
            data[3] = data[3].strip("\n")                     # Removing \n which was tagged with the each entry
            task = Task(data[0], data[1], data[2], data[3])
            task_list.append(task)
        file.close()
    except FileNotFoundError:
        print("No Entries")                         # In case the file does not exist
    return task_list


def write_as_data(entries):
    file = open("../resources/Todolist.txt", "w")
    for entry in entries:
        file.write(entry.to_string())
    file.close()
