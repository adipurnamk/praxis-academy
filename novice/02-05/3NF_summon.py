#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='123', database='3NF')
cursor = mariadb_connection.cursor()

number = 0
cursor.execute("SELECT t1.Full_Names, t2.Movies_Rented FROM Table1 t1, Table2 t2 WHERE t1.ID = t2.ID and t1.Full_Names='JanetJones';")
for Full_Names, Movies_Rented in cursor:
    number += 1
    # print(number, "{}rented {}".format(Full_Names, Movies_Rented))
    print("{}".format(Full_Names))
    print(number, "{}".format(Movies_Rented))