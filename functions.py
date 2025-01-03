FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read the text file and return a list of to-do """
    with open(filepath, "r") as file_r:
        todos_read = file_r.readlines()
    return todos_read

def write_todos(todos_write, filepath_w=FILEPATH):
    """ Write the to-do list to the text file"""
    with open(filepath_w, "w") as file_w:
        file_w.writelines(todos_write)


if __name__ == "__main__":
    print(get_todos())