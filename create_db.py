import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    port='5000',
    user = "root",
    passwd = "VIT_Vellore21",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE pyxis")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)