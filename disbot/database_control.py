from pymongo import MongoClient
import os

cluster = MongoClient(
    "mongodb://AlfriendOMat:{}@disbot.3e3gv.mongodb.net/DisBot?retryWrites=true&w=majority".format(
        os.getenv("DB_PASS")))
db = cluster["DisBot"]


def add_encouragement(encouragement):
    collection = db["Encouragements"]
    if collection.find_one({}):
        if not collection.find_one({"encouragement": encouragement}):
            enc_id = len(collection.find_many({}))
            collection.insert_one({"_id": enc_id, "encouragement": encouragement})
    else:
        collection.insert_one({"_id": 0, "encouragement": encouragement})
    return


def delete_encouragement(index):
    collection = db["Encouragements"]
    encouragements = collection.find_many({})
    if len(encouragements) > index:
        collection.delete_one({"_id": index})
    return


def get_encouragements():
    collection = db["Encouragements"]
    encouragements = []
    results = collection.find({})
    for result in results:
        print(result)
        encouragements.append(result)
    return encouragements
