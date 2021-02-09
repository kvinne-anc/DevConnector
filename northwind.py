import sqlite3

#Connecting to sqlite3
conn = sqlite3.connect('nw_proper.sqlite3')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

header = """
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
"""
result = cursor.execute(header).fetchall()

print("RESULT", result)


cat = """
SELECT sql FROM sqlite_master WHERE name="Customer"
"""
result1 = cursor.execute(cat).fetchall()

print("RESULT", result1)

#- `expensive_items`: What are the ten most expensive items (per unit price) in the database?

cat1 = """
SELECT sql FROM sqlite_master WHERE name="OrderDetail"
"""
result2 = cursor.execute(cat1).fetchall()

print("RESULT", result2)

expensive_items = """
SELECT *
FROM OrderDetail
ORDER BY UnitPrice DESC
LIMIT 10
"""

result3 = cursor.execute(expensive_items).fetchall()
print("MOST EXPENSIVE ITEMS", result3)

# `avg_hire_age`: What is the average age of an employee at the time of their hiring? (Hint: a
 # lot of arithmetic works with dates.)
 #Hire date minus birthdate = age at hire, then sum the result and divide by number of employees 

#Tells me what is in the Employee table 
cat2 = """
SELECT sql FROM sqlite_master WHERE name="Employee"
"""
result4 = cursor.execute(cat2).fetchall()

print("RESULT", result4)

#Age at date of hire function 
hiring_age = """
SELECT HireDate, BirthDate,
(HireDate - BirthDate)
FROM Employee
"""
result5 = cursor.execute(hiring_age).fetchall()

print("AGE AT HIRE", result5)

#Average age at hire - noticed that these hire dates are in the future... not sure if that is a glitch or just because it's fake data? 

avg_age = """
SELECT avg(HireDate - BirthDate)
FROM Employee 
"""
result6 = cursor.execute(avg_age).fetchall()

print("AVG AGE AT HIRE", result6)

#(*Stretch*) `avg_age_by_city`: How does the average age of employee at hire vary by city?

avg_age_by_city = """
SELECT avg(HireDate - BirthDate)
FROM Employee 
GROUP BY City 
"""
result7 = cursor.execute(avg_age_by_city).fetchall()

print("AVG AGE BY CITY", result7)

