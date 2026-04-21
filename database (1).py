import sqlite3

# Connect to SQLite database
def get_connection():
    return sqlite3.connect("students.db", check_same_thread=False)

# Create table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()

# Insert data
def add_student(name, age, course):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()

# Fetch all students
def get_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

# Update student
def update_student(id, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, id)
    )
    conn.commit()
    conn.close()

# Delete student
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()