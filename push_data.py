import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi #certifi python package that provides a set of root certificates, commonly used by python libraries that need to make a secure http connection
ca = certifi.where() #trusted ca == certificate authorities

#as we are importing data also
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = data.to_dict(orient="records") #converting each records to json here (key - value pair)
            return  records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL) # creating a client to connect with  mongodb using the localhost url

            db = self.mongo_client[database]
            col = db[collection]

            # 🔥 ACTUAL INSERT HAPPENS HERE
            result = col.insert_many(records)

            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
   

if __name__ == "__main__":
    FILE_PATH = os.path.join("Network_Data", "phisingData.csv")
    DATABASE = "RAM_AI"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)

    print(f"Records read from CSV: {len(records)}")

    no_of_records = networkobj.insert_data_mongodb(
        records=records,
        database=DATABASE,
        collection=COLLECTION
    )

    print(f"✅ Inserted {no_of_records} records into MongoDB")

