import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

#Python opens a conenction to database.db
def get_db__connection():
    connection = sqlite3.connect("database.db")
    #allows us to work with database results using the column names
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/courses", methods=["GET", "POST"])
def courses():

    if request.method == "POST":
        action = request.form["action"] 

        if action == "delete":
            course_id = request.form["course_id"]

            connection = get_db__connection()

            connection.execute(
                "DELETE FROM courses WHERE id = ?",
                (course_id,)
            )

            connection.commit()
            connection.close()

        else: 
            name = request.form["name"]
            description = request.form["description"]

            #Helps prevent errors
            if not name:
                return "Course name is required."

            connection = get_db__connection()

            existing_course = connection.execute(
                "SELECT * FROM courses WHERE name = ?",
                (name,)
            ).fetchone()

            if existing_course:
                connection.close()
                return "A course with that name already exists."
            
            
            connection.execute(
                "INSERT INTO courses (name, description) VALUES (?, ?)",
                (name, description)
            )
            
            connection.commit()
            connection.close()
        

    connection = get_db__connection()

    courses = connection.execute(
        "SELECT * FROM courses"
    ).fetchall()

    connection.close()

    return render_template("courses.html", courses=courses)

@app.route("/sessions", methods=["GET", "POST"])
def sessions():

    if request.method == "POST":
        course_id = request.form["course_id"]
        date = request.form["date"]
        duration = request.form["duration"]
        notes = request.form["notes"]

        if not course_id or not date or not duration:
            return "Please fill out all required fields."

        try:
             duration = int(duration)
        except ValueError:
            return "Study duration must be a number."
        
        if int(duration) <= 0:
            return "Study duration must be greater than 0 minutes."

        connection = get_db__connection()
                    
        connection.execute(
            "INSERT INTO sessions (course_id, date, duration, notes) VALUES (?, ?, ?, ?)",
            (course_id, date, duration, notes)
        )
                    
        connection.commit()
        connection.close()

    connection = get_db__connection()

    courses = connection.execute(
        "SELECT * FROM courses"
    ).fetchall()

    sessions = connection.execute(
        """
        SELECT sessions.date, sessions.duration, sessions.notes, courses.name
        FROM sessions
        JOIN courses ON sessions.course_id = courses.id
        """
    ).fetchall()

    connection.close()

    return render_template("sessions.html", courses=courses, sessions=sessions)


if __name__ == "__main__":
    app.run(debug=True)