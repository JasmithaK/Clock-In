import sqlite3

connection = sqlite3.connect("database.db") 

#Creating Tables
connection.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    duration INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (course_id) REFERENCES courses (id) 
)
""")

connection.commit()
connection.close()