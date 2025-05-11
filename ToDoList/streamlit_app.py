import streamlit as st
import django
import os
import sys
from django.conf import settings

# Django setup
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

from todo_app.models import User, Task

# Simple session state
if 'user' not in st.session_state:
    st.session_state.user = None

def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if User.objects.filter(username=username).exists():
            st.error("Username already exists.")
        else:
            user = User(username=username, email=email, password=password)
            user.save()
            st.success("Account created. Please log in.")

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = User.objects.get(username=username, password=password)
            st.session_state.user = user
            st.success(f"Logged in as {user.username}")
        except User.DoesNotExist:
            st.error("Invalid credentials.")

def logout():
    st.session_state.user = None
    st.success("Logged out.")

def todo_app():
    st.title("📝 ToDo List")

    if st.button("Logout"):
        logout()
        return

    st.subheader("Add Task")
    title = st.text_input("Task Title")
    content = st.text_area("Task Content")
    if st.button("Add Task"):
        Task.objects.create(user=st.session_state.user, title=title, content=content)
        st.success("Task added.")

    st.subheader("Your Tasks")
    tasks = Task.objects.filter(user=st.session_state.user)
    for task in tasks:
        st.write(f"**{task.title}** - {task.content}")

# Router
if st.session_state.user:
    todo_app()
else:
    page = st.sidebar.radio("Navigation", ("Login", "Sign Up"))
    if page == "Login":
        login()
    elif page == "Sign Up":
        signup()
