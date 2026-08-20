import sqlite3

connection = sqlite3.connect("database.db") 

#Testing adding data into courses
#connection.execute(
#   "INSERT INTO courses (name, description) VALUES (?, ?)",
#   ("MATH 218", "Calculus")
#)

#connection.commit()
#connection.close()

#Testing fetching data from courses
#cursor = connection.execute(
#    "SELECT id, name, description FROM courses"
#)

#courses = cursor.fetchall()

#for course in courses:
#    print(course)

#connection.close()

#Testing adding data into sessions
#connection.execute(
#   "INSERT INTO sessions (course_id, date, duration, notes) VALUES (?, ?, ?, ?)",
#   (1, "7/25/26", 75, "Reviewed integrals")
#)

#connection.commit()
#connection.close()

#Testing fetching data from sessions
cursor = connection.execute(
    "SELECT id, course_id, date, duration, notes FROM sessions"
)

sessions = cursor.fetchall()

for session in sessions:
    print(session)

connection.close()