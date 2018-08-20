from flask import Flask, render_template, request, session, redirect
from helpers import login_required, db_connect

from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from numbers import Number
import sqlite3

app = Flask(__name__)
# totaal random
app.secret_key = b'3RT6HJ8L'

@app.route("/")
@login_required
def test():
    return render_template("input.html")

@app.route("/rekening")
@login_required
def rekening():
    return render_template("rekening.html")

@app.route("/login", methods=["POST","GET"])
def login():
    db = db_connect('pythonsqlite.db')
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # check for complete form better in JS
        if not request.form.get("username") or not request.form.get("password"):
            return render_template("retry.html")
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          (request.form.get("username"),))
        # Ensure username exists and password is correct
        row = rows.fetchone()
        if not row or not check_password_hash(row[2], request.form.get("password")):
            return render_template("retry.html")

        # Remember which user has logged in
        session["user_id"] = request.form.get("username")

        # Redirect user to home page
        return redirect("/")

@app.route("/register", methods=["POST","GET"])
def register():
    conn = sqlite3.connect('pythonsqlite.db')
    db = conn.cursor()
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        # check for complete form better in JS
        if not request.form.get("username") or not request.form.get("password"):
            return render_template("retry.html")
        elif not request.form.get("password") == request.form.get("confirmation"):
            return render_template("retry.html")
        # Generate hash
        hash = generate_password_hash(request.form.get("password"))

        # Insert user into database
        rows = db.execute("INSERT INTO users (username, hash) VALUES(?,?)",
                          (request.form.get("username"), hash))
        # commit changes
        conn.commit()
        if not rows:
            return render_template("retry.html")

        # Remember which user has logged in
        session["user_id"] = request.form.get("username")

        # Redirect user to home page
        return redirect("/")

@app.route("/home")
@login_required
def home():
    render_template("home.html")