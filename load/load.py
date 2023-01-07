import pandas as pd 
import psycopg2
import csv

from utils import connection_object

conn = connection_object()

cur = conn.cursor()

#requête pour récupérer les données à partir de la table
cur.execute("SELECT * FROM TWEET_INFO")

# Récupérez les en-têtes de colonne de la table
headers = [desc[0] for desc in cur.description]

# Utilisez la bibliothèque csv pour écrire les données dans un fichier CSV
with open('data/file.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(cur)

# Fermez la connexion à la base de données
conn.close()