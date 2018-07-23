from flask import Flask, render_template, request, session, redirect
from helpers import login_required

app = Flask(__name__)
app.secret_key = b'3RT6HJ8L'
@app.route("/")
@login_required
def test():
    return render_template("test.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # check for complete form better in JS
        if not request.form.get("username") or not request.form.get("password"):
            return render_template("retry.html")
        session["user_id"] = request.form.get("username")# need to change
        return redirect("/")
