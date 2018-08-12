from flask import Flask, render_template, request, session, redirect
from helpers import login_required, db_connect


app = Flask(__name__)
# totaal random
app.secret_key = b'3RT6HJ8L'
@app.route("/")
@login_required
def test():
    db = db_connect('pythonsqlite.db')
    return render_template("input.html")

@app.route("/login", methods=["POST","GET"])
def login():
    db = db_connect('pythonsqlite.db')
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # check for complete form better in JS
        if not request.form.get("username") or not request.form.get("password"):
            return render_template("retry.html")
        # set vars for shorter lines
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("SELECT * FROM users WHERE username='%s'" % username)
        row = db.fetchone()
        # check for valid username and password
        if row and row[2] == password:
            session["user_id"] = request.form.get("username")# need to change
            return redirect("/")
        else:
            return render_template("retry.html")# should be incorrect username or password
