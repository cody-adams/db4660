from pymongo import Connection
connection = Connection()
#Create database and collections if they don't already exist
db = connection['db4660']
stu_collec = db['students']
cla_collec = db['classes']
fac_collec = db['faculty']
dep_collec = db['departments']
#write one document to each collection to actually have it be created
stu_results = db.stu_collec.insert_one({"test":"test"})
cla_results = db.cla_collec.insert_one({"test":"test"})
fac_results = db.fac_collec.insert_one({"test":"test"})
dep_results = db.dep_collec.insert_one({"test":"test"})
