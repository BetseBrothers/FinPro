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

@app.route("/", methods=["POST","GET"])
@login_required
def test():
    db = db_connect('pythonsqlite.db')
    rows = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                        (session["user_id"],))
    rekeningen = rows.fetchall()
    return render_template("input.html", rekeningen=rekeningen)

@app.route("/rekening", methods=["POST","GET"])
@login_required
def rekening():
    if request.method == "POST":
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        # Insert rekening into database
        db.execute("INSERT INTO rekeningen (userid, balans, rekeningnaam) VALUES(?,0,?)",
                          (session["user_id"], request.form.get("naam")))
        # commit changes
        conn.commit()
        
        return render_template("rekening.html")
    else:
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
        session["user_id"] = row[0]

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
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          (request.form.get("username"),))
        row = rows.fetchone()
        # Remember which user has logged in
        session["user_id"] = row[0]

        # Redirect user to home page
        return redirect("/")

@app.route("/home")
@login_required
def home():
    db = db_connect('pythonsqlite.db')
    rowsb = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                          (session["user_id"],))
    rowb = rowsb.fetchall()
    balans = 0
    schmekkels = 0
    for row in rowb:
        if not row[2] == "smekkels":
            balans += row[1]
        else:
            schmekkels = row[1]
    return render_template("home.html", balans=balans, schmekkels=schmekkels)
@app.route("/balans")
@login_required
def balans():
    db = db_connect('pythonsqlite.db')
    rowsb = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                          (session["user_id"],))
    rowb = rowsb.fetchall()
    balans = 0
    for row in rowb:
        if not row[2] == "smekkels":
            balans += row[1]
    rekeningtotaal = 0
    for row in rowb:
        if not row[2] == "smekkels" and not row[2] == "cash":
            rekeningtotaal += row[1]
    return render_template("balans.html", rekeningen=rowb, totaal=balans, rekeningtotaal=rekeningtotaal)
@app.route("/budget")
@login_required
def budget():
    return render_template("budget.html")