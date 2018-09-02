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
        return redirect("/home")

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
    # Bereken cash
    db = db_connect('pythonsqlite.db')
    rowsb = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                          (session["user_id"],))
    rowb = rowsb.fetchall()
    balans = 0
    for row in rowb:
        balans += row[1]
    # Bereken beleggingen TODO
    # Bereken totaalbudget
    rowsb = db.execute("SELECT * FROM Budgetten WHERE Userid = ?",
                          (session["user_id"],))
    budgetten = rowsb.fetchall()
        # Bereken totaal van alle budgetten
    totaalbudget = 0
    for row in budgetten:
        totaalbudget += row[2]
    # Bereken totaaluitgaven huidige maand
    selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month')",
                          (session["user_id"], "Uitgave"))
    uitgaven = selecteer.fetchall()
    totaaluitgaven = 0
    for uitgave in uitgaven:
        totaaluitgaven += uitgave[2]
    # bereken totaal van inkomsten in huidige maand
    selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month')",
                        (session["user_id"], "Inkomst"))
    inkomsten = selecteer.fetchall()
    totaalinkomsten = 0
    for inkomst in inkomsten:
        totaalinkomsten += inkomst[2]
    # Inkomsten
    rowsb = db.execute("SELECT * FROM Inkomsten WHERE userid = ? ",
                        (session["user_id"],))
    rowb = rowsb.fetchone()
    inkomst = rowb[1]
    # Inkomstenhuidig
    # Savings
    # Savingshuidig
    # maand
    dbm = db_connect('pythonsqlite.db')
    rowsm = dbm.execute("SELECT * FROM transacties WHERE userid=? AND Datum >= date('now','start of month') AND Datum < date('now','start of month','+1 month')", (session["user_id"],))
    rowm = rowsm.fetchall()
    maandI = 0
    maandU = 0
    for row in rowm:
        if row[5] == "Inkomst":
            maandI += row[2]
        else:
            maandU += row[2]
    # jaar
    dbj = db_connect('pythonsqlite.db')
    rowsj = dbj.execute("SELECT * FROM transacties WHERE userid=? AND Datum >= date('now','start of month') AND Datum < date('now','start of month','+1 month')", (session["user_id"],))
    rowj = rowsj.fetchall()
    jaarI = 0
    jaarU = 0
    for row in rowj:
        if row[5] == "Inkomst":
            jaarI += row[2]
        else:
            jaarU += row[2]
    # Neem alle beleggingen van huidige user voor op pagina te zetten
    rowsb = db.execute("SELECT * FROM Beleggingen WHERE Userid = ?",
                          (session["user_id"],))
    beleggingen = rowsb.fetchall()
    # Bereken totaal van alle portfolios: prijs en waarde
    totaalbeleggingen = 0
    totaalprijs = 0
    totaalverkocht = 0
    for row in beleggingen:
        totaalprijs += row[2]
        totaalbeleggingen += row[3]
        totaalverkocht += row[6]
    return render_template("home.html", totaalprijs=totaalprijs, totaalbeleggingen=totaalbeleggingen, totaalverkocht=totaalverkocht,  balans=balans, totaalbudget=totaalbudget, totaaluitgaven=totaaluitgaven, totaalinkomsten=totaalinkomsten, inkomst=inkomst, maandI=maandI, maandU=maandU, jaarI=jaarI, jaarU=jaarU, date=time.strftime("%x"), month=time.strftime("%b"))
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
        if not row[2] == "smekkels" and not row[2] == "Cash":
            rekeningtotaal += row[1]
    # Bereken totaal van inkomsten en uitgaven aller tijden
    db = db_connect('pythonsqlite.db')
    selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=?",
                            (session["user_id"], "Inkomst"))
    inkomsten = selecteer.fetchall()
    alltimeinkomsten = 0
    for inkomst in inkomsten:
        alltimeinkomsten += inkomst[2]
    selecteer2 = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=?",
                            (session["user_id"], "Uitgave"))
    uitgaven = selecteer2.fetchall()
    alltimeuitgaven = 0
    for uitgave in uitgaven:
        alltimeuitgaven += uitgave[2]
    # Neem alle beleggingen van huidige user voor op pagina te zetten
        rowsb = db.execute("SELECT * FROM Beleggingen WHERE Userid = ?",
                          (session["user_id"],))
        beleggingen = rowsb.fetchall()
    # Bereken totaal van alle portfolios: prijs en waarde
    totaalbeleggingen = 0
    totaalprijs = 0
    totaalverkocht = 0
    for row in beleggingen:
        totaalprijs += row[2]
        totaalbeleggingen += row[3]
        totaalverkocht += row[6]
    return render_template("balans.html", totaalprijs=totaalprijs, totaalbeleggingen=totaalbeleggingen, totaalverkocht=totaalverkocht, rekeningen=rowb, totaal=balans, rekeningtotaal=rekeningtotaal, inkomsten=alltimeinkomsten, uitgaven=alltimeuitgaven)
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
        db = db_connect('pythonsqlite.db')
        rowsb = db.execute("SELECT * FROM Budgetten WHERE userid = ? ",
                          (session["user_id"],))
        rowb = rowsb.fetchall()
        # for loop met budgetten: voor elk budget: iterate over alle categorieën en select transacties als nt NULL
        budgethuidigen = []
        i = 0
        for budget in rowb:
            budgethuidigen.append(0)
            for categorie in range(32):
                if budget[categorie + 3] is not "NULL":
                    select = db.execute("SELECT * FROM Transacties WHERE userid=? and Subcategorie=? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month')",
                          (session["user_id"], budget[categorie + 3]))
                    transacties = select.fetchall()
                    for transactie in transacties:
                        budgethuidigen[i] += transactie[2]
            i = i + 1
        totaalhuidigbudget = sum(budgethuidigen)
        # bereken totaal van uitgaven in huidige maand
        selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month')",
                          (session["user_id"], "Uitgave"))
        uitgaven = selecteer.fetchall()
        totaaluitgaven = 0
        for uitgave in uitgaven:
            totaaluitgaven += uitgave[2]
        # bereken totaal van inkomsten in huidige maand
        selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=? and Datum >= date('now','start of month') and Datum < date('now','start of month','+1 month')",
                          (session["user_id"], "Inkomst"))
        inkomsten = selecteer.fetchall()
        totaalinkomsten = 0
        for inkomst in inkomsten:
            totaalinkomsten += inkomst[2]
        return render_template("budget.html", inkomsten=inkomst, inkomhuidig=inkomhuidig, budgetten=budgetten, totaalbudget=totaalbudget, budgethuidigen=budgethuidigen, totaalhuidigbudget=totaalhuidigbudget, totaaluitgaven=totaaluitgaven, totaalinkomsten=totaalinkomsten)
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

@app.route("/jaar")
@login_required
def jaar():
    db = db_connect('pythonsqlite.db')
    dbU = db_connect('pythonsqlite.db')
    rowsI = db.execute("SELECT * FROM Transacties WHERE userid=? AND soort='Inkomst'", (session["user_id"],))
    rowsU = dbU.execute("SELECT * FROM Transacties WHERE userid=? AND soort='Uitgave'", (session["user_id"],))
    transacties = rowsI.fetchall()
    transactiesU = rowsU.fetchall()
    return render_template("jaar.html", transacties=transacties, Uitgaven=transactiesU, date=time.strftime("%x"))
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

@app.route("/overschrijving", methods=["POST","GET"])
@login_required
def overschrijving():
    if request.method == "GET":
        db = db_connect('pythonsqlite.db')
        rows = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                            (session["user_id"],))
        rekeningen = rows.fetchall()
        return render_template("overschrijving.html", rekeningen=rekeningen)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        db.execute('UPDATE rekeningen SET balans=balans+? where rekeningnaam=? AND userid=?', 
                        (request.form.get("Hoeveelheid"), request.form.get("naar"), session["user_id"]))
        conn.commit()
        db.execute('UPDATE rekeningen SET balans=balans-? where rekeningnaam=? AND userid=?', 
                        (request.form.get("Hoeveelheid"), request.form.get("van"), session["user_id"]))
        conn.commit()
        return redirect("/balans")
@app.route("/lening")
@login_required
def lening():
    return render_template("lening.html")
@app.route("/portfolio", methods=["POST","GET"])
@login_required
def portfolio():
    if request.method == "GET":
        return render_template("portfolio.html")
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        db.execute("INSERT INTO Portfolios (userid, naam) VALUES(?,?)",
                          (session["user_id"], request.form.get("naam")))
        # commit changes
        conn.commit()
        return redirect("/beleggingen")
@app.route("/beleggingen", methods=["POST","GET"])
@login_required
def beleggingen():
    if request.method == "GET":
        db = db_connect('pythonsqlite.db')
        rowsb = db.execute("SELECT * FROM Portfolios WHERE userid = ? ",
                            (session["user_id"],))
        portfolios = rowsb.fetchall()
        # Neem alle beleggingen van huidige user voor op pagina te zetten
        rowsb = db.execute("SELECT * FROM Beleggingen WHERE Userid = ?",
                          (session["user_id"],))
        beleggingen = rowsb.fetchall()
        # Bereken totaal van alle portfolios: prijs en waarde
        totaalbeleggingen = 0
        totaalprijs = 0
        totaalverkocht = 0
        for row in beleggingen:
            totaalprijs += row[2]
            totaalbeleggingen += row[3]
            totaalverkocht += row[6]
        # Bereken cash
        rowsb = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                          (session["user_id"],))
        rowb = rowsb.fetchall()
        cash = 0
        for row in rowb:
            cash += row[1]
        # Bereken 12 laatste maanden aan uitgaven
        selecteer = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=? and Datum >= date('now','start of month', '-12 month') and Datum < date('now','start of month')",
                          (session["user_id"], "Uitgave"))
        uitgaven = selecteer.fetchall()
        totaaluitgaven = 0
        for uitgave in uitgaven:
            totaaluitgaven += uitgave[2]
        return render_template("beleggingen.html", portfolios=portfolios, beleggingen=beleggingen, totaalprijs=totaalprijs, totaalbeleggingen=totaalbeleggingen, cash=cash, totaaluitgaven=totaaluitgaven, totaalverkocht=totaalverkocht)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        db.execute('UPDATE Beleggingen SET waarde=? where naam=? AND userid=?', 
                        (request.form.get("update"), request.form.get("naam"), session["user_id"]))
        # commit changes
        conn.commit()
        # voeg nieuwe status toe aan historiek
        # Neem alle beleggingen van huidige user voor op pagina te zetten
        rowsb = db.execute("SELECT * FROM Beleggingen WHERE Userid = ?",
                          (session["user_id"],))
        beleggingen = rowsb.fetchall()
        # Bereken totaal van alle portfolios: prijs en waarde
        totaalbeleggingen = 0
        for row in beleggingen:
            totaalbeleggingen += row[3]
        # Bereken cash
        rowsb = db.execute("SELECT * FROM rekeningen WHERE userid = ? ",
                          (session["user_id"],))
        rowb = rowsb.fetchall()
        cash = 0
        for row in rowb:
            cash += row[1]
        # Steek in historiek voor huidige datum
        db.execute("INSERT INTO Historiek (userid, cash, beleggingen, datum) VALUES(?,?,?,date('now'))",
                            (session["user_id"], cash, totaalbeleggingen))
        # commit changes
        conn.commit()
        return redirect("/beleggingen")
@app.route("/addbelegging", methods=["POST","GET"])
@login_required
def addbelegging():
    if request.method == "GET":
        db = db_connect('pythonsqlite.db')
        rowsb = db.execute("SELECT * FROM Portfolios WHERE userid = ? ",
                            (session["user_id"],))
        portfolios = rowsb.fetchall()
        rowsb = db.execute("SELECT * FROM Rekeningen WHERE userid = ? ",
                            (session["user_id"],))
        rekeningen = rowsb.fetchall()
        rowsb = db.execute("SELECT * FROM Beleggingen WHERE userid = ? ",
                            (session["user_id"],))
        beleggingen = rowsb.fetchall()
        return render_template("addbelegging.html", portfolios=portfolios, rekeningen=rekeningen, beleggingen=beleggingen)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        if request.form.get("belegging") == "nieuw":
            db.execute('UPDATE rekeningen SET balans=balans-? where rekeningnaam=? AND userid=?', 
                        (request.form.get("Bedrag"), request.form.get("rekening"), session["user_id"]))
            db.execute("INSERT INTO Beleggingen (userid, naam, prijs, waarde, portfolio, datum, verkocht) VALUES(?,?,?,?,?,date('now'), 0.0)",
                            (session["user_id"], request.form.get("naam"), request.form.get("Bedrag"), request.form.get("Waarde"), request.form.get("portfolios")))
        else:
            db.execute('UPDATE rekeningen SET balans=balans-? where rekeningnaam=? AND userid=?', 
                        (request.form.get("Bedrag"), request.form.get("rekening"), session["user_id"]))
            db.execute('UPDATE Beleggingen SET prijs=prijs+? where naam=? AND userid=?', 
                        (request.form.get("Bedrag"), request.form.get("belegging"), session["user_id"]))
            db.execute('UPDATE Beleggingen SET waarde=waarde+? where naam=? AND userid=?', 
                        (request.form.get("Waarde"), request.form.get("belegging"), session["user_id"]))
        # commit changes
        conn.commit()
        return redirect("/beleggingen")
@app.route("/verkoopbelegging", methods=["POST","GET"])
@login_required
def verkoopbelegging():
    if request.method == "GET":
        db = db_connect('pythonsqlite.db')
        rowsb = db.execute("SELECT * FROM Portfolios WHERE userid = ? ",
                            (session["user_id"],))
        portfolios = rowsb.fetchall()
        rowsb = db.execute("SELECT * FROM Rekeningen WHERE userid = ? ",
                            (session["user_id"],))
        rekeningen = rowsb.fetchall()
        rowsb = db.execute("SELECT * FROM Beleggingen WHERE userid = ? ",
                            (session["user_id"],))
        beleggingen = rowsb.fetchall()
        return render_template("verkoopbelegging.html", portfolios=portfolios, rekeningen=rekeningen, beleggingen=beleggingen)
    else:
        conn = sqlite3.connect('pythonsqlite.db')
        db = conn.cursor()
        db.execute('UPDATE Beleggingen SET verkocht=verkocht+? where naam=? AND userid=?', 
                        (request.form.get("verkocht"), request.form.get("belegging"), session["user_id"]))
        db.execute('UPDATE rekeningen SET balans=balans+? where rekeningnaam=? AND userid=?', 
                        (request.form.get("bedrag"), request.form.get("rekening"), session["user_id"]))
        # commit changes
        conn.commit()
        return redirect("/beleggingen")
@app.route("/grafiek")
@login_required
def grafiek():
    db = db_connect('pythonsqlite.db')
    rows = db.execute("SELECT * FROM Transacties WHERE userid=? AND soort='Uitgave'", (session["user_id"],))
    uitgaven = rows.fetchall()
    # bereken totaal van inkomsten in huidige maand
    inkomst = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=?",
                        (session["user_id"], "Inkomst"))
    ink = inkomst.fetchall()
    # bereken totaal van uitgaven in huidige maand
    uitgave = db.execute("SELECT * FROM Transacties WHERE userid=? and Soort=?",
                          (session["user_id"], "Uitgave"))
    uit = uitgave.fetchall()
    return render_template("grafiek.html", uitgaven=uitgaven, ink=ink, uit=uit, date=time.strftime("%x"))
