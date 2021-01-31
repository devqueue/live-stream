# pip install mysql-connector-python

import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", password="c9070baa", database="Haziq") 

if con.is_connected():
    print("connection successful")
    cursor  = con.cursor()
    cursor.execute("select * from GAMES")
    data = cursor.fetchall()
    print(data)
