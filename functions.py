

todo = []
fh = open('todos.txt').readlines()
for line in fh:
    cleaned_line = line.strip()
    if cleaned_line:  # Check if the line is not empty after stripping
        todo.append(cleaned_line)


def display_list_format():

    formatted_l = []
    for index, item in enumerate(todo):
        formatted_item = f"{index + 1}. {item}"
        formatted_l.append(formatted_item)
    return '\n'.join(formatted_l)

def add_item(k):
    todo.append(k)
    return todo

def delete_item(b):

    todo.pop(b-1)
    return todo


def write_file():
   with open('todos.txt', 'w') as fh1:
      for todo_list_item in todo:
        fh1.write(todo_list_item+'\n' )
      return fh1.close()