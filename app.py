import os

from flask import Flask, render_template, request, redirect
from config import db, cursor

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template("index.html", active_page="home")

# About
@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

# Courses
@app.route("/courses")
def courses():
    return render_template("courses.html", active_page="courses")

# Gallery
@app.route("/gallery")
def gallery():
    return render_template("gallery.html", active_page="gallery")

# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html", active_page="contact")

# Admission Page
@app.route("/admission")
def admission():
    return render_template("admission.html", active_page="admission")


# Admission Form Submit
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    course = request.form["course"]
    message = request.form["message"]

    query = """
    INSERT INTO admissions
    (name,email,phone,course,message)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(name,email,phone,course,message))
    db.commit()

    return render_template("success.html", active_page="admission")


# Admin Login Page
@app.route("/admin")
def admin():
    return render_template("admin_login.html", active_page="admin")


# Admin Login
@app.route("/adminlogin", methods=["POST"])
def adminlogin():

    username = request.form["username"]
    password = request.form["password"]

    query = "SELECT * FROM admin WHERE username=%s AND password=%s"

    cursor.execute(query,(username,password))

    admin = cursor.fetchone()

    if admin:
        return redirect("/dashboard")
    else:
        return render_template("admin_login.html", error="Invalid username or password", active_page="admin")


# Admin Dashboard
@app.route("/dashboard")
def dashboard():

    cursor.execute("SELECT * FROM admissions")

    data = cursor.fetchall()

    return render_template("dashboard.html", data=data, active_page="admin")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )