import pandas as pd 

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pprintpp import pprint 

load_dotenv()

#DB_NAME = os.getenv("DB_NAME", default="OOPS") 
#A lot of messing around - never explains why this line is removed 
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/atlas0?retryWrites=true&w=majority"
#connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@a{CLUSTER_NAME}.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
#This is the 'client =' code strip from mongo to connect to application - the variables in the brackets are hidden in the env file 

print("-----------") 
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)


db = client.test_database

collection1 = db.test_collection1 
print("------------")
print("COLLECTION1:", type(collection1), collection1)

pprint(dir(collection1))



print("DOCS:", collection1.count_documents({}))

#mongoimport --connection_uri --collection("Titanic") --type(dict:Dict[str, Any]) --file(C:\Users\surfb\lambdata_kvinneDPST9\my_lambdata\TitanicMongo) 



#print(db.list_collection_names())

titanic = pd.read_csv('titanic.csv')

print(titanic)

mongoimport --help



