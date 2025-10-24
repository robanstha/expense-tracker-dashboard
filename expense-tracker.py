import streamlit as st
import datetime
import pandas as pd

st.set_page_config(page_title="Daily Habit Tracker", page_icon="✅", layout="centered")

st.title("✅ Daily To-Do & Habit Tracker")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input new task
with st.form("new_task_form"):
    task = st.text_input("Add a new task or habit")
    submitted = st.form_submit_button("Add Task")
    if submitted and task:
        st.session_state.tasks.append({"task": task, "done": False, "date": datetime.date.today()})

# Display task list
st.subheader("Today's Tasks")
if len(st.session_state.tasks) == 0:
    st.info("No tasks yet. Add something above 👆")
else:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"- {t['task']}")
        with col2:
            st.session_state.tasks[i]["done"] = st.checkbox("Done", value=t["done"], key=f"chk_{i}")

# Summary
completed = sum(t["done"] for t in st.session_state.tasks)
total = len(st.session_state.tasks)
st.progress(completed / total if total else 0)
st.write(f"**{completed} / {total} tasks completed today.**")

# Option to clear finished tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.experimental_rerun()
