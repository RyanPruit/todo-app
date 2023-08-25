import functions as f

while True:

    action = input("What action do you want to do:show,edit,add,delete,exit")+'\n'
    action = action.strip()

    match action:

        case 'show':
            print(f.display_list_format())
        case 'add':
            t = input("Enter to do:")
            f.add_item(t)
            f.write_file()
        case 'delete':
            user_delete = int(input("Which to do item you want to delete from the list:"))
            print("Here is the list:-")
            f.delete_item(user_delete)
            f.write_file()
            print(f.display_list_format())
        case 'exit':
            print("bye")
            break




