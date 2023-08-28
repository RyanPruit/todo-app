
import functions
import streamlit as st
st.title("My To-Do App")

def add_todo():
    x = st.session_state['new_todo'] +'\n'
    functions.todo.append(x)
    functions.write_file()

for index, do in enumerate(functions.todo):

    checkbox = st.checkbox(do,key=index)

    if checkbox:
        functions.todo.pop(index)
        functions.write_file()
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",on_change=add_todo,key='new_todo')



