from os import write

FILEPATH = 'todo.txt'

def get(filepath = FILEPATH):

    with open(filepath) as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print("hello")
    print(get())


