import psygopg2

connection = psycopg2.connect(dbname=klmfogwy, user=klmfogwy, password=tZUY3hKexZiJKcrU65qulMOJKhGMS218, host=ziggy.db.elephantsql.com)
print("CONNECTION", type(connection))

cursor = connection.cursor()

