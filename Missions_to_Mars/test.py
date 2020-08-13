import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

output = {'test':'Testy McTesterpants'}

# Define the 'MarsDB' database in Mongo
db = client.MarsDB
missions = db.mission.find()
# print(missions)
# db.mission.insert_one(output)

for mission in missions:
    msg = mission
    # t = msg['tweet']

print(msg['headline'])