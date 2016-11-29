import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
cnx = mysql.connector.connect(user='root', password='hello', database='db4660', host='127.0.0.1')
cursor = cnx.cursor(buffered=True)
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
for _ in range(1000):
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
print "Average time to insert a record into students 1000 times is: {}".format(students_insert/1000)
faculty_insert = datetime.now()
for _ in range(100):
    first_part=sd['fname'][random.randint(0,len(sd['fname'])-1)]
    second_part=sd['lname'][random.randint(0,len(sd['lname'])-1)]
    before = datetime.now()
    cursor.execute("INSERT INTO faculty (fname,lname,age,addr) VALUES('{}','{}',{},'yes')".format(first_part, second_part,random.randint(0,99)))
    after = datetime.now()
    if (_==0):
        faculty_insert = after - before
    else:
        faculty_insert += after - before    
print "Average time to insert a record into faculty 100 times is: {}".format(faculty_insert/100)
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
for _ in range(50):
    before = datetime.now()
    cursor.execute("INSERT INTO depts (dname) VALUES('{}')".format(deps[random.randint(0,len(deps)-1)]))
    after = datetime.now()
    if (_==0):
        depts_insert = after - before
    else:
        depts_insert += after - before
print "Average time to insert a record into departments 50 times is: {}".format(depts_insert/50)
clas=[
    'CPSC4660',
    'PHIL1000',
    'JPN1000',
    'CPSC3655',
    'CPSC2720',
    'MATH2000',
    'JPN1500',]

for _ in range(200):
    before = datetime.now()
    cursor.execute("INSERT INTO classes (cname,cno) VALUES('{}',{})".format(clas[random.randint(0,len(clas)-1)],_))
    after = datetime.now()
    if (_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Average time to insert a record into classes 200 times is: {}".format(classes_insert/200)
for _ in range(1000):
    cursor.execute("INSERT INTO takes (cno,sid) VALUES({},{})".format(random.randint(0,39),_))
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
    cursor.execute("SELECT * FROM takes WHERE sid in (SELECT sid FROM students)")
    after = datetime.now()
    if (_==0):
        join_insert = after - before
    else:
        join_insert += after - before
print "Selecting values out of Takes with sids matching from students, 100 times averages: {}".format(join_insert/100)
large_join = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor.execute("SELECT * FROM students INNER JOIN takes ON students.sid=takes.sid INNER JOIN classes ON classes.cno=takes.cno")
    after = datetime.now()
    for document in cursor:
        n = 1
    if (_==0):
        large_join = after - before
    else:
        large_join += after - before
print "Joining 3 tables 100 times on average takes {}".format(large_join/100)

largest_join = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor.execute("SELECT * FROM students INNER JOIN takes ON students.sid=takes.sid INNER JOIN classes ON classes.cno=takes.cno INNER JOIN teaches ON classes.cno=teaches.cno INNER JOIN faculty ON teaches.fid=faculty.fid")
    after = datetime.now()
    for document in cursor:
        n = 1
    if (_==0):
        largest_join = after - before
    else:
        largest_join += after - before
print "Joining 5 tables 100 times on average takes {}".format(largest_join/100)
before = datetime.now()
cursor.execute("DELETE FROM students WHERE sid = 99")
after = datetime.now()
print "Deleting a record from table students takes: {} ".format(after - before)
cursor.execute("DROP TABLES students")
cursor.execute("DROP TABLES classes")
cursor.execute("DROP TABLES depts")
cursor.execute("DROP TABLES takes")
cursor.execute("DROP TABLES faculty")
cursor.close()
cnx.close()
