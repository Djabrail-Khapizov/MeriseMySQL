# Système d’Information JO Milano-Cortina 2026 Djabrail KHAPIZOV, Shiva ILANCHEJIAN

## Présentation

Ce projet a pour objectif de concevoir et d’implémenter un système d’information pour les Jeux Olympiques d’hiver 2026 de Milano-Cortina.

Le projet couvre plusieurs parties :

- analyse métier ;
- modélisation Merise ;
- création d’une base MySQL ;
- requêtes SQL ;
- optimisation avec index et EXPLAIN ;
- mini application web Flask connectée à MySQL ;
- réflexion Big Data / analytique.

---

# Fonctionnalités

L’application permet actuellement :

- d’afficher les athlètes enregistrés dans la base ;
- d’afficher les épreuves olympiques ;
- d’afficher les médailles par pays ;
- de vérifier la connexion entre Flask et MySQL.

---

# Structure du projet

```text
MYSQL_MERISE/
│
├── app_jo/
│   ├── app.py
│   └── templates/
│       ├── base.html
│       └── index.html
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies utilisées

- Python
- Flask
- MySQL
- MySQL Workbench
- HTML
- Bootstrap
- Git / GitHub

---

# Prérequis

Avant de lancer le projet, il faut avoir installé :

- Python 3
- MySQL Server
- MySQL Workbench
- Git

---

# Installation de l’environnement Python

Installer les dépendances :

```bash
pip install flask mysql-connector-python
```

---

# Configuration de la base de données

Créer la base MySQL :

```sql
CREATE DATABASE jo_milano_2026;
USE jo_milano_2026;
```

Ensuite, exécuter les scripts SQL permettant de créer les tables et d’insérer les données de test.

---

# Configuration de la connexion MySQL

Dans le fichier :

```text
app_jo/app.py
```

modifier les informations de connexion :

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="VOTRE_MOT_DE_PASSE",
    database="jo_milano_2026"
)
```

⚠️ Le mot de passe MySQL personnel ne doit pas être publié sur GitHub.  
Il doit être remplacé localement par chaque utilisateur.

---

# Lancer l’application Flask

Depuis la racine du projet :

```bash
cd app_jo
```

Puis lancer :

```bash
python app.py
```

Ou sur Windows si nécessaire :

```bash
py app.py
```

L’application sera disponible à l’adresse :

```text
http://127.0.0.1:5000
```

---

# Sécurité

Pour un projet réel, il faudrait améliorer la sécurité avec :

- un fichier `.env` pour les identifiants ;
- des mots de passe hashés ;
- des requêtes paramétrées ;
- une gestion des rôles utilisateurs ;
- ne jamais exposer les identifiants de base de données dans un dépôt public.


---

# Auteur

Djabrail KHAPIZOV, Shiva ILANCHEJIAN