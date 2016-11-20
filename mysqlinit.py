from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
cnx = mysql.connector.connect(user='root', password='hello', database='db4660', host='127.0.0.1')
tables = {}
tables['students'] =( "CREATE TABLE `students` ("
"  `sid` int(11) NOT NULL AUTO_INCREMENT,"
"  `fname` varchar(25) NOT NULL,"
"  `lname` varchar(50) NOT NULL,"
"  `age` int(10) NOT NULL,"
"  `addr` varchar(50) DEFAULT NULL,"
"  PRIMARY KEY (`sid`)"
"  ) ENGINE=InnoDB")
tables['faculty'] =( "CREATE TABLE `faculty` ("
"`fid` int(11) NOT NULL AUTO_INCREMENT,"
"`fname` varchar(25) NOT NULL,"
"`lname` varchar(50) NOT NULL,"
"`age` int(10) NOT NULL,"
"`addr` varchar(50) DEFAULT NULL,"
"PRIMARY KEY (`fid`)"
") ENGINE=InnoDB")
tables['classes'] =( "CREATE TABLE `classes` ("
"`cname` varchar(25) NOT NULL,"
"`cno` int(11) NOT NULL,"
"PRIMARY KEY (`cno`)"
") ENGINE=InnoDB")
tables['depts'] =( "CREATE TABLE `depts` ("
"`dname` varchar(25) NOT NULL,"
"`did` int(11) NOT NULL AUTO_INCREMENT,"
"PRIMARY KEY (`did`)"
") ENGINE=InnoDB")
tables['takes'] =( "CREATE TABLE `takes` ("
                   "`cno` int(11) NOT NULL,"
                   "`sid` int(11) NOT NULL,"
                   "PRIMARY KEY (cno,sid)"
                   ") ENGINE-InnoDB")
cursor = cnx.cursor()
DB_NAME='db4660'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
for name, ddl in tables.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
        cursor.execute("show tables")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
cursor.close()
cnx.close()
