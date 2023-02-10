import csv
import mysql.connector

# configuration data for logging in
config = {
    'user': 'unknown',
    'password': 'unknown',
    'host': '127.0.0.1',
    'database': 'unknown',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("Desired query")

cursor.execute(query)

for values in cursor:
    print(values)

cursor.close()
cnx.close()
