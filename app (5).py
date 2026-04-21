import streamlit as st
import database as db

db.create_table()

st.title(" Student Management System")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

# ADD
if choice == "Add Student":
    st.subheader("Add New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    course = st.text_input("Course")

    if st.button("Add"):
        db.add_student(name, age, course)
        st.success("Student added successfully!")

# VIEW
elif choice == "View Students":
    st.subheader("All Students")
    students = db.get_students()
    st.table(students)

# UPDATE
elif choice == "Update Student":
    st.subheader("Update Student")
    students = db.get_students()
    ids = [s[0] for s in students]

    student_id = st.selectbox("Select Student ID", ids)
    name = st.text_input("New Name")
    age = st.number_input("New Age", min_value=1)
    course = st.text_input("New Course")

    if st.button("Update"):
        db.update_student(student_id, name, age, course)
        st.success("Student updated!")

# DELETE
elif choice == "Delete Student":
    st.subheader("Delete Student")
    students = db.get_students()
    ids = [s[0] for s in students]

    student_id = st.selectbox("Select Student ID", ids)
    if st.button("Delete"):
        db.delete_student(student_id)
        st.success("Student deleted!")