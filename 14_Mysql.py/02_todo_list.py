import mysql.connector

connection = mysql.connector.connect(host = "localhost",user = "root",password = "12345678",database = "todo")
# to check the connection is establish or not 
if connection.i_connected():
    print("database is connected")
else:
    print("database is not connected")

task = "create table if not exists task(task_name text)"

#create cursor to execute the mysql query
my_cursor = connection.cursor()

#to execute the create table in database todo
my_cursor.execute(task)

#to commit or save the mysql query
connection.commit()