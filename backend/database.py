from pymongo import MongoClient
import json
import os


db_host = 'localhost'
db_port = 27017  #Default MongoDB port
db_name = 'powerflex'


class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            #Establish connection to mongo database
            cls._instance.client = MongoClient(os.environ['MONGO_HOST'])
            cls._instance.db = cls._instance.client[os.environ['MONGO_NAME']]

        return cls._instance
    
    def seed_data(self, collection_name, json_path):
        #Extract data from seed_data json files
        with open (json_path) as file:
            data = json.load(file)

        #Set up database collection
        collection = self.db[collection_name]

        #Check if the data already exists
        if collection.count_documents({}) > 0:
            print("Data already seeded. Skipping...")
            return

        #Insert the data into the collection
        collection.insert_many(data)

    def add_data(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def delete_data(self, collection_name, filter=None):
        collection = self.db[collection_name]
        collection.delete_many(filter)

    def update_data(self, collection_name, filter, update_data):
        collection = self.db[collection_name]
        collection.update_one(filter, {"$set": update_data})

    def get_data(self, collection_name, filter=None):
        collection = self.db[collection_name]
        cursor = collection.find(filter, {'_id': 0})
        data = list(cursor)
        return data
    
    def check_data(self, collection_name, filter):
        if self.get_data(collection_name, filter):
            return True
        return False
    
    def print_data(self, collection_name, filter=None):
        collection = self.db[collection_name]
        cursor = collection.find(filter, {'_id': 0})
        data = list(cursor)
        print(data)

    def destroy_data(self):
        self.client.drop_database(os.environ['MONGO_NAME'])