FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Retrieves the todos from the file and stores in a variable
    :param filepath: The path of the file to get the todos from
    :type filepath: str
    :return: To-do list from the given filepath
    :rtype: list
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the given todos in a text file
    :param todos_arg: list of todos to write in the text file
    :type todos_arg: list
    :param filepath: The path of the text file for the todos to be stored
    :type filepath: str
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


# __name__ variable holds the name of the module that is being executed \
#   - when function.py is imported from another file: __name__ will not be "__main__"
if __name__ == "__main__":
    print("Main Module is functions.py")
