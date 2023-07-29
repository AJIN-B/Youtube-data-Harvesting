
from pymongo import MongoClient


def mdb_insert(keyword,channel_Data,video_Data,comments_data):

    client = MongoClient("localhost", 27017)

    db = client['youtube']
    collection_names = db.list_collection_names()

    # Find the first available name by appending a number
    new_collection_name = keyword
    counter = 1
    while new_collection_name in collection_names:
        new_collection_name = f"{keyword}{counter}"
        counter += 1 
        
    # Create the collection with the new name
    collection = db[new_collection_name]
    Channel_Data = {"_id":f"{new_collection_name}-Channel","Channels_Data":channel_Data}
    collection.insert_one(Channel_Data)
    
    # Videos_Data = {"_id":f"{new_collection_name}-Videos","Videos_Data":video_Data}
    # Comments_Data = {"_id":f"{new_collection_name}-Comments","Comments_Data":comments_data}
    ## insert at document level
    # coll_Data = [Channel_Data,Videos_Data,Comments_Data]

    # for col in coll_Data:
    #     collection.insert_one(col)


