import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
cnx = mysql.connector.connect(user='root', password='hello', database='db4660', host='127.0.0.1')
cursor = cnx.cursor()
cursor.execute("set autocommit = 1")
cursor.execute("DROP TABLES IF EXISTS students")
cursor.execute("DROP TABLES IF EXISTS classes")
cursor.execute("DROP TABLES IF EXISTS depts")
cursor.execute("DROP TABLES IF EXISTS takes")
cursor.execute("DROP TABLES IF EXISTS faculty")
