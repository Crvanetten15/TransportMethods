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

file_path = input('What file do we need to pull data from to MySQL: ')

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    # Creating the table if not existing
    table_name = input(f'enter table name for {file_path}')
    columns = ','.join([f"{col} VARCHAR(255)" for col in header])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

    # Inserting rows of data into the table
    for row in reader:
        values = ','.join([f"'{value}'" for value in row])
        cursor.execute(
            f"INSERT INTO {table_name} ({','.join(header)}) VALUES ({values})")

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
