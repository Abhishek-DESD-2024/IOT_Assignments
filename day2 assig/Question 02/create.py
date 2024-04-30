# Write a python program to add, delete, update employees into table

# import module of mysql connector



import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb"
)

# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter the department:")
email = input("Enter email :")
sallary = int(input("Enter sallary : "))
date_of_joining = input("Enter the date and time:")

query = f"insert into employees values({empid}, '{name}', '{department}', '{email}', {sallary}, '{date_of_joining}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()









