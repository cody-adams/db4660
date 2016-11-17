from pymongo import Connection
connection = Connection()

db = connection['db4660']
stu_collec = db['students']
cla_collec = db['classes']
fac_collec = db['faculty']
dep_collec = db['departments']

stu_results = db.stu_collec.insert_one({
"fname":"",
"lname":"",
"age":"",
"addr":""})

cla_results = db.cla_collec.insert_one({
"cname":"",
"cno":""})

fac_results = db.fac_collec.insert_one({
"fname":"",
"lname":"",
"age":"",
"addr":""})

dep_results = db.dep_collec.insert_one({
"dname":"",
})

