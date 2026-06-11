from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://adyashanayak165_db_user:veIll0H0rptkaDZa@cluster0.mzt5imv.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)