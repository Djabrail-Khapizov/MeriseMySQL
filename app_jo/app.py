from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MOT_DE_PASSE", # Remplacez par votre mot de passe MySQL
        database="jo_milano_2026"
    )

@app.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.nom, a.prenom, p.nom AS pays
        FROM athlete a
        JOIN pays p ON a.id_pays = p.id_pays
    """)
    athletes = cursor.fetchall()

    cursor.execute("""
        SELECT e.nom AS epreuve, s.nom AS sport, site.nom AS site
        FROM epreuve e
        JOIN sport s ON e.id_sport = s.id_sport
        JOIN site ON e.id_site = site.id_site
    """)
    epreuves = cursor.fetchall()

    cursor.execute("""
        SELECT p.nom AS pays, COUNT(m.id_medaille) AS nb_medailles
        FROM medaille m
        JOIN athlete a ON m.id_athlete = a.id_athlete
        JOIN pays p ON a.id_pays = p.id_pays
        GROUP BY p.nom
    """)
    medailles = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "index.html",
        athletes=athletes,
        epreuves=epreuves,
        medailles=medailles
    )

if __name__ == "__main__":
    app.run(debug=True)