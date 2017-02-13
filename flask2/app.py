import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)

conn = sqlite3.connect('lab.db')


class Personne:
    def __init__(self, prenom, nom, age):
        self.prenom = prenom
        self.nom = nom
        self.age = age


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET'])
def create():
    return render_template("create.html")


@app.route('/create', methods=['POST'])
def create_post():

    saved_prenom = request.form["prenom"]
    return render_template("create.html", default_prenom=saved_prenom)


@app.route('/list')
def list():
    cursor = conn.cursor()
    cursor.execute("select * from personne")

    personnes = []
    for row in cursor:
        p = Personne(row[1], row[2], row[3])
        personnes.append(p)

    return render_template("list.html", personnes=personnes)

if __name__ == '__main__':
    app.run()
