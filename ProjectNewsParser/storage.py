from storage_data import storage_data
from sentence_info import sentence_info
import pymongo
from dotenv import load_dotenv
import os


def store(url, db_obj):
    load_dotenv()
    mongo_url = os.environ.get('MONGO_URL')
    mongo_username = os.environ.get('MONGO_USERNAME')
    mongo_password = os.environ.get('MONGO_PASSWORD')
    db_name = os.environ.get('MONGO_DB')

    client = pymongo.MongoClient(mongo_url, username=mongo_username, password=mongo_password)
    db = client[db_name]
    collection = db["articles"]

    where = {"url": url}
    update = {"$set": db_obj}
    collection.update_one(filter=where, update=update, upsert=True)
