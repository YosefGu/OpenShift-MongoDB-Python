from pymongo import MongoClient
import os

class DataLoader:

    def __init__(self):
        self.client = MongoClient(
            host=os.getenv("MONGO_HOST"),
            username=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASSWORD"),
        )
        self.db = self.client[os.getenv("MONGO_DATABASE", "test_db")]
        self.collection = self.db["users"]

    def get_data(self):
        return list(self.collection.find({}, {"_id": 0})) 

    def add_data(self, user):
        try:
            doc = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            self.collection.insert_one(doc)
            return True
        except Exception as e:
            print("Error:", e)
            return e
