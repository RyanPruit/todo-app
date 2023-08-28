
import functions
import streamlit as st
st.title("My To-Do App")

def add_todo():
    x = st.session_state['new_todo']
    functions.todo.append(x)
    functions.write_file()

for do in functions.todo:
    st.checkbox(do)


st.text_input(label="",placeholder="Add new todo...",on_change=add_todo,key='new_todo')



