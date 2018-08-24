from flask import Flask, render_template, request, session, redirect
from helpers import login_required, db_connect

from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from numbers import Number
import sqlite3
import time

app = Flask(__name__)
# totaal random
app.secret_key = b'3RT6HJ8L'

@app.route("/", methods=["POST","GET"])
@login_required
def test():
    if request.method == "GET":
        db = db_connect('pythonsqlite.db')
        rows = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                            (session["user_id"],))
        rekeningen = rows.fetchall()
        return render_template("input.html", rekeningen=rekeningen)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        # Insert transactie into database
        db.execute("INSERT INTO Transacties (Userid, Naam, Bedrag, Datum, Rekening, Soort, Categorie, Subcategorie) VALUES(?,?,?,?,?,?,?,?)",
                          (session["user_id"], request.form.get("name"), request.form.get("Hoeveelheid"), request.form.get("Datum"), request.form.get("rekening"), request.form.get("soort"), request.form.get("Categorie"), request.form.get("Subcategorie")))
        # commit changes
        conn.commit()
        rows = db.execute("SELECT * FROM rekeningen where userid=? AND rekeningnaam=?",
                            (session["user_id"], request.form.get("rekening")))
        balans = rows.fetchone()
        if request.form.get("soort") == "Uitgave":
            newbalans = balans[1] - float(request.form.get("Hoeveelheid"))
        else:
            newbalans = balans[1] + float(request.form.get("Hoeveelheid"))
        db.execute("UPDATE rekeningen SET balans=? WHERE userid=? AND rekeningnaam=?",
                          (newbalans, session["user_id"], request.form.get("rekening")))
        # commit changes
        conn.commit()
        return render_template("home.html")

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
@app.route("/budget", methods=["POST","GET"])
@login_required
def budget():
    if request.method == "GET":
        # Get data for Inkomsten
        db = db_connect('pythonsqlite.db')
        rowsb = db.execute("SELECT * FROM Inkomsten WHERE userid = ? ",
                          (session["user_id"],))
        rowb = rowsb.fetchone()
        inkomst = rowb[1]
        # Get data for Status van inkomsten: enkel voor huidige maand
        rowsb = db.execute("SELECT * FROM Transacties WHERE Userid = ? and Soort = ? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month') ",
                          (session["user_id"], "Inkomst",))
        rowb = rowsb.fetchall()
        inkomhuidig = 0
        for row in rowb:
            inkomhuidig += row[2]
        # Neem alle budgetten van huidige user voor op pagina te zetten
        rowsb = db.execute("SELECT * FROM Budgetten WHERE Userid = ?",
                          (session["user_id"],))
        budgetten = rowsb.fetchall()
            # Bereken totaal van alle budgetten
        totaalbudget = 0
        for row in budgetten:
            totaalbudget += row[2]
        # Selecteer alle budgetten en selecteer voor elke categorie erin alle transacties van huidige maand
        # en voeg toe aan totaal van dat budget

        # Zet bij juiste budgetten
            # Bereken huidige totaal van budgetten
        return render_template("budget.html", inkomsten=inkomst, inkomhuidig=inkomhuidig, budgetten=budgetten, totaalbudget=totaalbudget)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        # Delete last income
        db.execute("DELETE FROM Inkomsten WHERE userid=?",
                          (session["user_id"],))
        conn.commit()
        # Insert transactie into database
        db.execute("INSERT INTO Inkomsten (userid, inkomsten) VALUES(?,?)",
                            (session["user_id"], request.form.get("inkomsten")))
        # commit changes
        conn.commit()
        return redirect("/budget")
@app.route("/maand")
@login_required
def maand():
    db = db_connect('pythonsqlite.db')
    dbU = db_connect('pythonsqlite.db')
    rowsI = db.execute("SELECT * FROM Transacties WHERE userid=? AND soort='Inkomst'", (session["user_id"],))
    rowsU = dbU.execute("SELECT * FROM Transacties WHERE userid=? AND soort='Uitgave'", (session["user_id"],))
    transacties = rowsI.fetchall()
    transactiesU = rowsU.fetchall()
    return render_template("maand.html", transacties=transacties, Uitgaven=transactiesU, date=time.strftime("%x"))
@app.route("/addbudget", methods=["POST","GET"])
@login_required
def addbudget():
    if request.method == "GET":
        return render_template("addbudget.html")
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        # Insert new income
        db.execute("INSERT INTO Budgetten (userid, naam, bedrag, restaurant, winkel, openbaarVervoer, auto, verzekering, dokters, kleren, abonnementen, diensten, elektronica, gsm, huisdieren, elektriciteit, huis, water, internet, meubels, supplies, vuilnis, games, sport, tekenen, reizen, tuin, events, lezen, tv, onderwijs, charity, belasting, gift, interest) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                          (session["user_id"], request.form.get("naam"), request.form.get("bedrag"), request.form.get("restaurant"), request.form.get("winkel"), request.form.get("openbaarVervoer"), request.form.get("auto"), request.form.get("verzekering"), request.form.get("dokters"), request.form.get("kleren"), request.form.get("abonnementen"), request.form.get("diensten"), request.form.get("elektronica"), request.form.get("gsm"), request.form.get("huisdieren"), request.form.get("elektriciteit"), request.form.get("huis"), request.form.get("water"), request.form.get("internet"), request.form.get("meubels"), request.form.get("supplies"), request.form.get("vuilnis"), request.form.get("games"), request.form.get("sport"), request.form.get("tekenen"), request.form.get("reizen"), request.form.get("tuin"), request.form.get("events"), request.form.get("lezen"), request.form.get("tv"), request.form.get("onderwijs"), request.form.get("charity"), request.form.get("belasting"), request.form.get("gift"), request.form.get("interest")))
        # commit changes
        conn.commit()
        return redirect("/budget")
@app.route("/verwijderbudget", methods=["POST"])
@login_required
def verwijderbudget():
    conn = sqlite3.connect('pythonsqlite.db')
    db = conn.cursor()
    # Delete budget
    db.execute("DELETE FROM Budgetten WHERE userid=? and naam=?",
                        (session["user_id"], request.form.get("verwijder")))
    conn.commit()
    return redirect("/budget")