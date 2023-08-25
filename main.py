
todo = []
fh = open('todos.txt').readlines()
for line in fh:
    cleaned_line = line.strip()
    if cleaned_line:  # Check if the line is not empty after stripping
        todo.append(cleaned_line)



def display_list_format(x):

    formatted_l = []
    for index, item in enumerate(x):
        formatted_item = f"{index + 1}. {item}"
        formatted_l.append(formatted_item)
    return '\n'.join(formatted_l)

def add_item(k):
    todo.append(k)
    return todo


def write_file(td):
   with open('todos.txt', 'w') as fh1:
      for todo_list_item in todo:
        fh1.write(todo_list_item+'\n' )
      return fh1.close()


while True:

    action = input("What action do you want to do:show,edit,add,delete,exit")+'\n'
    action = action.strip()

    match action:

        case 'show':
            print(display_list_format(todo))
        case 'add':
            t = input("Enter to do:")
            add_item(t)
            write_file(todo)


        case 'delete':
            user_delete=int(input("Which to do item you want to delete from the list:"))
            print("Here is the list:-")
            todo.pop(user_delete-1)
            write_file(todo)
            print(display_list_format(todo))

        case 'exit':
            print("bye")
            break




