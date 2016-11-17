from pymongo import MongoClient
import random

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
for _ in range(100):
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
#Faculty
for _ in range(10):
    fname=d['fname'][random.randint(0,len(d['fname'])-1)]
    lname=d['lname'][random.randint(0,len(d['lname'])-1)]
    fac_results = db.faculty.insert_one({
        "fname": "{}".format(fname),
        "lname": "{}".format(lname),
        "age": random.randint(0,99),
        "fid": _
        })

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
for _ in range(5):
    dep_results = db.departments.insert_one({
        'dname':"{}".format(deps[_]),
        'did':"{}".format(_)
        })
    
#Insert courses
clas=[
    'CPSC4660',
    'PHIL1000',
    'JPN1000',
    'CPSC3655',
    'CPSC2720',
    'MATH2000',
    'JPN1500',]

for _ in range(20):
    cla_results = db.classes.insert_one({
        'cname':"{}".format(clas[random.randint(0,len(clas)-1)]),
        'cid':_
        })
import pymongo
cid = db.classes.find().sort([('cid', pymongo.DESCENDING)])[1]
print cid['cid']
stus = db.students.find()

#for document in stus:


cursor = db.students.find()
for document in cursor:
    print(document)
cursor = db.faculty.find()
for document in cursor:
    print(document)
cursor = db.departments.find()
for document in cursor:
    print(document)
cursor = db.classes.find()
for document in cursor:
    print(document)
print cid['cid']
