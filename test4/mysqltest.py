from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
cnx = mysql.connector.connect(user='root', password='hello', database='db4660', host='127.0.0.1')
cursor = cnx.cursor()
sd={
'fname':[
    'Cody',
    'ThuyVi',
    'Shawn',
    'Wyatt',
    'Jamie',
    'Geoff',
    'John',
    'Travis',
    'Laura',
    'Liam',
    'Sam',],
'lname':[
    'Adams',
    'Nguyen',
    'Higa',
    'Trombley',
    'Blue',
    'Chappell',
    'Oliver',
    'Willingham',
    'Bailey',
    'OBrien',
    'Reigel',],
}
import random
students_insert = datetime.now()
for _ in range(2000):
    first_part=sd['fname'][random.randint(0,len(sd['fname'])-1)]
    second_part=sd['lname'][random.randint(0,len(sd['lname'])-1)]
    #print('{} {}'.format(first_part, second_part))
    before = datetime.now()
    cursor.execute("INSERT INTO students (fname,lname,age,addr) VALUES('{}','{}',{},'yes')".format(first_part, second_part,random.randint(0,99)))
    after = datetime.now()
    if (_==0):
        students_insert = after - before
    else:
        students_insert += after - before
print "Average time to insert a record into students 2000 times is: {}".format(students_insert/2000)
faculty_insert = datetime.now()
for _ in range(200):
    first_part=sd['fname'][random.randint(0,len(sd['fname'])-1)]
    second_part=sd['lname'][random.randint(0,len(sd['lname'])-1)]
    before = datetime.now()
    cursor.execute("INSERT INTO faculty (fname,lname,age,addr) VALUES('{}','{}',{},'yes')".format(first_part, second_part,random.randint(0,99)))
    after = datetime.now()
    if (_==0):
        faculty_insert = after - before
    else:
        faculty_insert += after - before    
print "Average time to insert a record into faculty 200 times is: {}".format(faculty_insert/200)
deps=[
    'Math',
    'English',
    'Psychology',
    'Languages',
    'Some other stuff',
    'I liked gym as a kid',
    'Philosophy',
    'Psychics',
    'These are not departments',]
for _ in range(100):
    before = datetime.now()
    cursor.execute("INSERT INTO depts (dname) VALUES('{}')".format(deps[random.randint(0,len(deps))]))
    after = datetime.now()
    if (_==0):
        depts_insert = after - before
    else:
        depts_insert += after - before
print "Average time to insert a record into departments 100 times is: {}".format(depts_insert/100)
clas=[
    'CPSC4660',
    'PHIL1000',
    'JPN1000',
    'CPSC3655',
    'CPSC2720',
    'MATH2000',
    'JPN1500',]

for _ in range(400):
    before = datetime.now()
    cursor.execute("INSERT INTO classes (cname,cno) VALUES('{}',{})".format(clas[random.randint(0,len(clas))]))
    after = datetime.now()
    if (_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Average time to insert a record into classes 400 times is: {}".format(classes_insert/400)
cursor.execute("SELECT sid FROM students")
tmpcursor = cnx.cursor()
for (sid_value) in cursor:
    tmpcursor.execute("INSERT INTO takes (cno,sid) VALUES({},{})".format(random.randint(0,19),sid_value))
for _ in range(100):
    before = datetime.now()
    cursor.execute("SELECT * FROM classes")
    after = datetime.now()
    if (_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Selecting Classes 100 times averages to be: {}".format(classes_insert/100)
for _ in range(200):
    before = datetime.now()
    cursor.execute("SELECT * FROM classes")
    after = datetime.now()
    if (_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Selecting Classes 200 times averages to be: {}".format(classes_insert/200)
for _ in range(300):
    before = datetime.now()
    cursor.execute("SELECT * FROM classes")
    after = datetime.now()
    if (_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Selecting Classes 300 times averages to be: {}".format(classes_insert/300)
        
for _ in range(100):
    before = datetime.now()
    cursor.execute("SELECT * FROM takes WHERE sid in (SELECT sid FROM students))")
    after = datetime.now()
    if (_==0):
        join_insert = after - before
    else:
        join_insert += after - before
print "Selecting values out of Takes with sids matching from students, 100 times averages: {}".format(join_insert/100)

cursor.execute("DELETE * FROM students")
cursor.execute("DELETE * FROM classes")
cursor.execute("DELETE * FROM departments")
cursor.execute("DELETE * FROM takes")
cursor.execute("DELETE * FROM faculty")
cursor.close()
tmpcursor.close()
cnx.close()
