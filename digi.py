from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector

app = Flask(__name__)

# DATABASE CONNECTION
def db_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="saiteja@1603",
        database="digittence"
    )


# HOME
@app.route("/")
def home():
    return render_template("index.html")


# REGISTER PAGE
@app.route("/register.html")
def register_page():
    return render_template("register.html")


# REGISTER USER
@app.route("/submit", methods=["POST"])
def register_user():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO register (name,email,password) VALUES (%s,%s,%s)",
        (name,email,password)
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect("/login.html")


# LOGIN PAGE
@app.route("/login.html")
def login_page():
    return render_template("login.html")


# LOGIN
@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    conn = db_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        "SELECT * FROM register WHERE email=%s AND password=%s",
        (email,password)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        return render_template("dashboard.html")
    else:
        return render_template("login.html")


# DASHBOARD
@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")


# CLASSES PAGE
@app.route("/Classes.html")
def classes():

    conn = db_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM classes")
    classes = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("Classes.html", classes=classes)


# ADD CLASS
@app.route("/add_class", methods=["POST"])
def add_class():

    className = request.form["className"]

    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO classes (className) VALUES (%s)",
        (className,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect("/Classes.html")


# DELETE CLASS
@app.route("/delete_class/<int:id>")
def delete_class(id):

    conn = db_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM classes WHERE id=%s",(id,))

    conn.commit()
    cur.close()
    conn.close()

    return redirect("/Classes.html")


# STUDENTS PAGE
@app.route("/students/<int:class_id>")
def students(class_id):

    conn = db_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        "SELECT * FROM students WHERE class_id=%s",
        (class_id,)
    )

    students = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("students.html", students=students, class_id=class_id)


# ADD STUDENT
@app.route("/add_student/<int:class_id>", methods=["POST"])
def add_student(class_id):

    name = request.form["name"]
    roll = request.form["rollNo"]

    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name,rollNo,class_id) VALUES (%s,%s,%s)",
        (name,roll,class_id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return redirect(f"/students/{class_id}")


# DELETE STUDENT
@app.route("/delete_student/<int:id>/<int:class_id>")
def delete_student(id,class_id):

    conn = db_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=%s",(id,))

    conn.commit()
    cur.close()
    conn.close()

    return redirect(f"/students/{class_id}")


# CLASS DASHBOARD
@app.route("/class/<int:id>")
def class_dashboard(id):

    conn = db_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM classes WHERE id=%s",(id,))
    classData = cur.fetchone()

    cur.close()
    conn.close()

    return render_template("class.html", classData=classData)


from flask import Flask, render_template, request, redirect, url_for
from models import Subject, db

app = Flask(__name__)

@app.route("/subjects/<int:class_id>")
def subjects(class_id):
    subjects = Subject.query.filter_by(class_id=class_id).all()
    return render_template("subjects.html", subjects=subjects, class_id=class_id)


@app.route("/add_subject", methods=["POST"])
def add_subject():
    name = request.form["name"]
    class_id = request.form["class_id"]

    new_subject = Subject(name=name, class_id=class_id)
    db.session.add(new_subject)
    db.session.commit()

    return redirect(url_for("subjects", class_id=class_id))


# ---------------- STUDENTS API ----------------
@app.route("/api/students/<int:class_id>")
def get_students(class_id):

    conn = db_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        "SELECT id AS _id, name, rollNo FROM students WHERE class_id=%s",
        (class_id,)
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)


@app.route("/api/students", methods=["POST"])
def api_add_student():

    data = request.json
    name = data["name"]
    rollNo = data["rollNo"]
    class_id = data["class"]

    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name,rollNo,class_id) VALUES (%s,%s,%s)",
        (name,rollNo,class_id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message":"student added"})


# ---------------- ATTENDANCE ----------------
@app.route("/api/attendance", methods=["POST"])
def save_attendance():

    data = request.json

    class_id = data["class"]
    subject = data["subject"]
    date = data["date"]
    hours = data["hours"]

    conn = db_conn()
    cur = conn.cursor()

    for record in data["records"]:
        student = record["student"]
        status = record["status"]

        cur.execute(
            "INSERT INTO attendance (student_id,class_id,subject,date,status,hours) VALUES (%s,%s,%s,%s,%s,%s)",
            (student,class_id,subject,date,status,hours)
        )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message":"attendance saved"})


# ---------------- PAGES ----------------
@app.route("/attendance.html")
def attendance():
    return render_template("attendance.html")

@app.route("/subjects.html")
def subjects():
    return render_template("subjects.html")

@app.route("/reports.html")
def reports():
    return render_template("reports.html")



# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)