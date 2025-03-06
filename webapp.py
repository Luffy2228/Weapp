

import streamlit as st
import getit

todos = getit.get()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    getit.write_todos(todos)

st.title("my application")
st.subheader("this app ")
st.write("this app for the builder")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder = "something",
                on_change=add_todo, key='new_todo')

