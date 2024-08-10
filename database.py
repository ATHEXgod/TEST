from pymongo import MongoClient
from config.settings import MONGO_DB_URI

client = MongoClient(MONGO_DB_URI)
db = client['file_sharing_bot']
# data/database.py

roles = db['roles']
