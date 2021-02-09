import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('sprint.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Droping DEMDATA table if already exists.
cursor.execute("DROP TABLE IF EXISTS DEMDATA")

#Creating table as per requirement
sql ='''CREATE TABLE DEMDATA( 
   S CHAR(2) NOT NULL,
   X INT,
   Y INT
)'''

cursor.execute(sql)
print("Table created successfully........")

data ='''INSERT INTO DEMDATA (S, X, Y) VALUES
(
    'G',
    3,
    9
),
(
    'V',
    5,
    7
),
(
    'F',
    8,
    7
);
'''
cursor.execute(data)
print("Data added to table........")

#Commit your changes in the database
conn.commit()

#`row_count`: Count how many rows you have - it should be 3!
# `xy_at_least_5`: How many rows are there where both `x` and `y` are at least 5?

query = """
SELECT
    count(*) as row_count
FROM DEMDATA

"""
result = cursor.execute(query).fetchall()

print("RESULT", result)

query1 = """
SELECT
    count(*) as row_count 
FROM DEMDATA
WHERE X > 4
"""
query01 = """
SELECT 
    count(*) as row_count
FROM DEMDATA 
WHERE Y > 4
"""
result1 = cursor.execute(query1).fetchall()

result01 = cursor.execute(query01).fetchall()

print("RESULT", result1, result01)

query2 = """
SELECT 
    count(*) as row_count
    ,count(Y) as val_y
    ,count(distinct Y) as unique_y
FROM DEMDATA

"""
result2 = cursor.execute(query2).fetchall()

print("RESULT", result2)

#Closing the connection
conn.close()


 

