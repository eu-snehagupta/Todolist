def read_to_file():
    file = open("../resources/Todolist.txt", "r")
    data = file.read()
    file.close()
    return data


def write_to_file(input_string):
    file = open("../resources/Todolist.txt", "a")
    file.write(input_string + "\n")
    file.close()


if __name__ == "__main__":
    print(read_to_file())
    write_to_file("hi?")