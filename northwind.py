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

#ten_most_expensive`: What are the ten most expensive items (per unit price) in the database *and* their suppliers?

cat8 = """
SELECT sql FROM sqlite_master WHERE name="Product"
"""
result8 = cursor.execute(cat8).fetchall()

print("RESULT", result8)

exp_item_supplier = """
SELECT UnitPrice, SupplierID
FROM Product
GROUP BY SupplierID
ORDER BY UnitPrice DESC
LIMIT 10
"""

result9 = cursor.execute(exp_item_supplier).fetchall()
print("MOST EXPENSIVE ITEMS BY SUPPLIER", result9)

# `largest_category`: What is the largest category (by number of unique products in it)?

cat9 = """
SELECT sql FROM sqlite_master WHERE name="Category"
"""
result10 = cursor.execute(cat9).fetchall()
print("RESULT", result10)

cat_uni_prod = """
SELECT 
    CategoryName,
    ProductName
FROM 
    Category
JOIN Product
    ON Category.ID = Product.CategoryID
GROUP BY CategoryID
ORDER BY QuantityPerUnit DESC;
"""
result11 = cursor.execute(cat_uni_prod).fetchall()
print("CAT BY PROD", result11)
print("THE CATEGORY WITH THE MOST PRODUCTS IS CONFECTIONS")

#The list shows that Confections has the most products and I can tell that this was correct because I ran multiple versions of this code to check and the result is not in alphabetical order which is a helpful indication. 
#double checking categories - there are 77 products 

### Part 4 - Questions (and your Answers)

# In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
print("The relationship between the Employee and Territory tables in the Northwind DB is encapsulated in the EmployeeTeritories table which would tell you which Employee covers which territory")
print("-------------")
#What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
print("A document store like MongoDB is useful if you are working with unstructured data like how Facebook can target you with political ads by keywords that you use or search for or accounts you click on - it can be more like mindmap analysis so if you search guns but click on a anti-gun account it won't push ads that are pro gun and will push political ads touting gun control, but if you search guns and click on pro-gun accounts it will push you ads for guns or political ads for preservation of the 2nd amendment. It would be inappropriate if say, I am using my input to structure the way a cellphone interface is structured and I need to be able to have things nested and connected and subgroups and not all will-nilly.")
print("-----------------")
#What is "NewSQL", and what is it trying to achieve?
print("NewSQL is a type of database language that aims to bring the best of both SQL and NoSQL together - the flexibility and scalability of NoSQL with the structure and organization of SQL.")

