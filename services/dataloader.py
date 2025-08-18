from pymongo import MongoClient
import os

class DataLoader:

    def __init__(self):
        self.client = MongoClient(
            host=os.getenv("MONGO_HOST"),
            username=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASSWORD"),
            authSource="admin"
        )
        self.db = self.client[os.getenv("MONGO_DATABASE", "test_db")]
        self.collection = self.db["users"]

    def get_data(self):
        return list(self.collection.find({}, {"_id": 0})) 
