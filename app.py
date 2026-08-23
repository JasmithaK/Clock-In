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
            
            connection = get_db__connection()
            
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

if __name__ == "__main__":
    app.run(debug=True)