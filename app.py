from flask import Flask, render_template

app = Flask ("__name__")

@app.route("/")

def HOME():
    return render_template("HOME.html")

@app.route("/quemsomos")

def quemsomos():
    return render_template("quemsomos.html")

@app.route("/Contato")

def contato():
    return render_template("Contato.html")