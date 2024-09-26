from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Fulo:Florina%403@cluster0.zrpn8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.todo_db
collection = db["todo_data"]
