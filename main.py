import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("TodoFlow")
st.subheader("A simple but impressive Todo manager")
st.write("This app increases your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

