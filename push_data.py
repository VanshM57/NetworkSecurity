# This file is used to push data from csv file to mongodb

import os 
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


import certifi
ca = certifi.where()

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
            raise NetworkSecurityException(e, sys)
        
#take data from csv file and convert it to json format
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            #reset index to ensure it starts from 0
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())    #alternative: records = json.loads(data.to_json(orient='records'))
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
#insert data into mongodb
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "networksecurity"
    Collection="NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records=records,database=DATABASE,collection=Collection)
    print(no_of_records)