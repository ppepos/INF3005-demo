import sqlite3

from flask import Flask, render_template


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

@app.route('/create')
def create():
    return render_template("create.html")

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

