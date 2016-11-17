from pymongo import MongoClient
client = MongoClient()
db = client['db4660']
#write one document to each collection to actually have it be created
stu_results = db.students.insert_one({"test":"test"})
cla_results = db.classes.insert_one({"test":"test"})
fac_results = db.faculty.insert_one({"test":"test"})
dep_results = db.departments.insert_one({"test":"test"})

print stu_results.inserted_id
print cla_results.inserted_id
print fac_results.inserted_id
print dep_results.inserted_id
