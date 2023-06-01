#Functions of to-do.py.
def get_todos(filepath="todos.txt"):
    """Reads the text file and returns the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg,filepath="todos.txt"):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#print(__name__)
if __name__ == "__main__" :
    print("Hello")
    print(get_todos())
