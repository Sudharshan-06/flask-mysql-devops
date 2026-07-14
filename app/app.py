from flask import Flask, render_template, request, redirect
from db import get_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_student():

    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        cursor.execute(
            "INSERT INTO students(name, age, course) VALUES(%s,%s,%s)",
            (name, age, course)
        )

        db.commit()

        return redirect("/students")

    return render_template("add_student.html")


@app.route("/students")
def students():

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        course VARCHAR(100)
    )
    """)

    db.commit()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return render_template("students.html", students=students)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
