from pymongo import MongoClient

# Local MongoDB connection (NO Atlas, NO internet)
client = MongoClient("mongodb://localhost:27017/")

# Test connection
try:
    client.admin.command("ping")
    print("✅ Connected to LOCAL MongoDB successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
    '''
    

# Optional: create DB & collection
db = client["networksecurity"]
collection = db["logs"]

collection.insert_one({(C:\projects\networksecurity\venv) C:\projects\networksecurity>python p
ush_data.py
✅ Connected to LOCAL MongoDB successfully!
✅ Data inserted into local MongoDB

(C:\projects\networksecurity\venv) C:\projects\networksecurity>  
    "status": "working",
    "type": "local_mongodb_test"
})

print("✅ Data inserted into local MongoDB")
'''
