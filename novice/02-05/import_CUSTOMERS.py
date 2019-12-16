#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='123', database='testDB')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT ID, AGE FROM CUSTOMERS WHERE SALARY = 2000.00;")
for ID, AGE in cursor:
    print("ID: {}, AGE: {}".format(ID,AGE))