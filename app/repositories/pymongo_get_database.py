
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser


def get_database():

   config = configparser.ConfigParser()
   config.read('credentials.ini')

   username = config.get('Credentials','username')
   password = config.get('Credentials','password')

   uri = f"mongodb+srv://{username}:{password}@cluster0.qg5hlm0.mongodb.net/"
   client = MongoClient(uri, server_api=ServerApi('1'))

   try:
        client.admin.command('ping')
        print("Pinged deployment. Successfully connected to MongoDB!")
   except Exception as e:
        print(e)

   return client['books_db']

  