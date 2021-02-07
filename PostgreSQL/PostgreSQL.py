import psycopg2
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd

load_dotenv()

DB_HOST = "ziggy.db.elephantsql.com"
DB_NAME = "klmfogwy"
DB_USER = "klmfogwy"
DB_PASSWORD = "tZUY3hKexZiJKcrU65qulMOJKhGMS218"

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

print("-------------------")
query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall()[0:10]:
    print(row)



#connection = psycopg2.connect(dbname=klmfogwy, user=klmfogwy, password=tZUY3hKexZiJKcrU65qulMOJKhGMS218, host=ziggy.db.elephantsql.com)
print("CONNECTION", type(connection))

cursor = connection.cursor()

