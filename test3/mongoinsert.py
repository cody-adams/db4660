from pymongo import MongoClient
import random
from datetime import datetime
client = MongoClient()
db = client.db4660

d={
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
#Students
students_insert = datetime.now()
for _ in range(1000):
    before = datetime.now()
    fname=d['fname'][random.randint(0,len(d['fname'])-1)]
    lname=d['lname'][random.randint(0,len(d['lname'])-1)]
    #print('{} {}'.format(fname, lname))
    stu_results = db.students.insert_one({
        "fname": "{}".format(fname),
        "lname": "{}".format(lname),
        "age": random.randint(0,99),
        "address": "ItsAllTheSame",
        "sid": _
        })
    after = datetime.now()
    if(_==0):
        students_insert = after - before
    else:
        students_insert += after - before
print "Average for insert 1000 students one by one is {}".format(students_insert/1000)
#Faculty
faculty_insert = datetime.now()
for _ in range(100):
    before = datetime.now()
    fname=d['fname'][random.randint(0,len(d['fname'])-1)]
    lname=d['lname'][random.randint(0,len(d['lname'])-1)]
    fac_results = db.faculty.insert_one({
        "fname": "{}".format(fname),
        "lname": "{}".format(lname),
        "age": random.randint(0,99),
        "fid": _
        })
    after = datetime.now()
    if(_==0):
        faculty_insert = after - before
    else:
        faculty_insert += after - before 
print "Average for insert 10 faculty one by one is {}".format(faculty_insert/100)
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
departments_insert = datetime.now()
for _ in range(50):
    before = datetime.now()
    dep_results = db.departments.insert_one({
        'dname':"{}".format(deps[random.randint(0,8)]),
        'did': _
        })
    after = datetime.now()
    if(_==0):
        departments_insert = after - before
    else:
        departments_insert += after - before    
print "Average for inserting 50 departments one by one is {}".format(departments_insert/50)
#Insert courses
clas=[
    'CPSC4660',
    'PHIL1000',
    'JPN1000',
    'CPSC3655',
    'CPSC2720',
    'MATH2000',
    'JPN1500',]
classes_insert = datetime.now()
for _ in range(200):
    before = datetime.now()
    cla_results = db.classes.insert_one({
        'cname':"{}".format(clas[random.randint(0,len(clas)-1)]),
        'cid':_,
        'did':random.randint(0,4)
        }) #Random.randint is to tie a class to a department, doesn't matter if the pair makes sense
    after = datetime.now()
    if(_==0):
        classes_insert = after - before
    else:
        classes_insert += after - before
print "Average for inserting 200 classes one by one is {}".format(classes_insert/200)
import pymongo
cid = db.classes.find().sort([('cid', pymongo.DESCENDING)])[1]
courses = cid['cid']
stus = db.students.find()

#for document in stus:
for document in stus:
    nCID = db.classes.find_one({"cid":random.randint(0,courses-1)})
    db.takes.insert_one({
        'cid': nCID['cid'],
        'sid': document['sid']
        })
facs = db.faculty.find()
for document in facs:
    nCID = db.classes.find_one({"cid":random.randint(0,courses-1)})
    db.teaches.insert_one({
        "cid": nCID['cid'],
        'fid': document['fid']
        })
get_students = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.students.find()
    after = datetime.now()
    if (_==0):
        get_students = after - before
    else:
        get_students += after - before

get_students_avg = get_students / 100
print "Getting students 100 times, averages to be {}".format(get_students_avg)
get_students = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.students.find()
    after = datetime.now()
    if (_==0):
        get_students = after - before
    else:
        get_students += after - before
get_students_avg = get_students / 200
print "Getting students 200 times, averages to be {}".format(get_students_avg)
get_students = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.students.find()
    after = datetime.now()
    if (_==0):
        get_students = after - before
    else:
        get_students += after - before
get_students_avg = get_students / 300
print "Getting students 300 times, averages to be {}".format(get_students_avg)

get_faculty = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.faculty.find()
    after = datetime.now()
    if (_==0):
        get_faculty = after - before
    else:
        get_faculty += after - before
get_faculty_avg = get_faculty / 100
print "Getting faculty 100 times, averages to be {}".format(get_faculty_avg)
get_faculty = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.faculty.find()
    after = datetime.now()
    if (_==0):
        get_faculty = after - before
    else:
        get_faculty += after - before
get_faculty_avg = get_faculty / 200
print "Getting faculty 200 times, averages to be {}".format(get_faculty_avg)
get_faculty = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.faculty.find()
    after = datetime.now()
    if (_==0):
        get_faculty = after - before
    else:
        get_faculty += after - before
get_faculty_avg = get_faculty / 300
print "Getting faculty 300 times, averages to be {}".format(get_faculty_avg)

#Getting departments 100, 200, and 300 times
get_departments = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.departments.find()
    after = datetime.now()
    if (_==0):
        get_departments = after - before
    else:
        get_departments += after - before
get_departments_avg = get_departments / 100
print "Getting departments 100 times, averages to be {}".format(get_departments_avg)
get_departments = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.departments.find()
    after = datetime.now()
    if (_==0):
        get_departments = after - before
    else:
        get_departments += after - before
get_departments_avg = get_departments / 200
print "Getting departments 200 times, averages to be {}".format(get_departments_avg)
get_departments = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.departments.find()
    after = datetime.now()
    if (_==0):
        get_departments = after - before
    else:
        get_departments += after - before
get_departments_avg = get_departments / 300
print "Getting departments 300 times, averages to be {}".format(get_departments_avg)

get_classes = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.classes.find()
    after = datetime.now()
    if (_==0):
        get_classes = after - before
    else:
        get_classes += after - before
get_classes_avg = get_classes / 100
print "Getting classes 100 times, averages to be {}".format(get_classes_avg)
get_classes = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.classes.find()
    after = datetime.now()
    if (_==0):
        get_classes = after - before
    else:
        get_classes += after - before
get_classes_avg = get_classes / 200
print "Getting classes 200 times, averages to be {}".format(get_classes_avg)
get_classes = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.classes.find()
    after = datetime.now()
    if (_==0):
        get_classes = after - before
    else:
        get_classes += after - before
get_classes_avg = get_classes / 300
print "Getting classes 300 times, averages to be {}".format(get_classes_avg)

get_takes = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.takes.find()
    after = datetime.now()
    if (_==0):
        get_takes = after - before
    else:
        get_takes += after - before
get_takes_avg = get_takes / 100
print "Getting takes 100 times, averages to be {}".format(get_takes_avg)
get_takes = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.takes.find()
    after = datetime.now()
    if (_==0):
        get_takes = after - before
    else:
        get_takes += after - before
get_takes_avg = get_takes / 200
print "Getting takes 200 times, averages to be {}".format(get_takes_avg)
get_takes = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.takes.find()
    after = datetime.now()
    if (_==0):
        get_takes = after - before
    else:
        get_takes += after - before
get_takes_avg = get_takes / 300
print "Getting takes 300 times, averages to be {}".format(get_takes_avg)
get_teaches = datetime.now()
for _ in range(100):
    before = datetime.now()
    cursor = db.teaches.find()
    after = datetime.now()
    if (_==0):
        get_teaches = after - before
    else:
        get_teaches += after - before
get_teaches_avg = get_teaches / 100
print "Getting teaches 100 times, averages to be {}".format(get_teaches_avg)
get_teaches = datetime.now()
for _ in range(200):
    before = datetime.now()
    cursor = db.teaches.find()
    after = datetime.now()
    if (_==0):
        get_teaches = after - before
    else:
        get_teaches += after - before
get_teaches_avg = get_teaches / 200
print "Getting teaches 200 times, averages to be {}".format(get_teaches_avg)
get_teaches = datetime.now()
for _ in range(300):
    before = datetime.now()
    cursor = db.teaches.find()
    after = datetime.now()
    if (_==0):
        get_teaches = after - before
    else:
        get_teaches += after - before
get_teaches_avg = get_teaches / 300
print "Getting teaches 300 times, averages to be {}".format(get_teaches_avg)
#Now do a query based on a result from 
#print cid['cid']
students_takes_avg = datetime.now()
times = 0
begin = datetime.now()
stu_res = db.students.find()
for document in stu_res:
    takes_res = db.takes.find({"sid":document['sid']})
after = datetime.now()
print "The time for joining students with takes is {}".format(after - begin)
   
begin = datetime.now()
stu2_res = db.students.find()
mval = 0
for document in stu2_res:
    if mval==0:
        takes2_res = db.takes.find({"sid":document['sid']})
        val = 1
    else:
        takes2_res += db.takes.find({"sid":document['sid']})
mval = 0
for document in takes2_res:
    if mval==0:
        classes2_res = db.takes.find({"cid":document['cid']})
        val = 1
    else:
        classes2_res += db.takes.find({"cid":document['cid']})
after = datetime.now()
print "The average time for joining students with takes with classes is {}".format(after - begin)
