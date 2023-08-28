
import functions
import streamlit as st
st.title("My To-Do App")

def add_todo():
    x = st.session_state['new_todo']
    functions.todo.append(x)
    functions.write_file()



def delete_todo():
    for index, do in enumerate(functions.todo):
        y = st.session_state[index]

        functions.todo.remove(y)
        functions.write_file()

for index, do in enumerate(functions.todo):

    checkbox = st.checkbox(do,key=index)

    if checkbox:
        functions.todo.remove(do)
        functions.write_file()



st.text_input(label="",placeholder="Add new todo...",on_change=add_todo,key='new_todo')+'\n'



