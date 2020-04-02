from .config import Config
from .utils.helper import Helper
from bson.objectid import ObjectId
import pymongo

class MongoHandler(object):

    def __init__(self):
        print(f"Connection to mongo: {Config}")
        self._mongo_client = pymongo.MongoClient(host=Config.DB_HOST,
                                                 port=Config.DB_PORT, # necessary
                                                 username=Config.DB_USERNAME,
                                                 password=Config.DB_PASSWORD,
                                                 authSource=Config.DB_NAME,
                                                 authMechanism=Config.DB_AUTH)

    def _user_collection(self):
        return self._mongo_client[Config.DB_NAME][Config.DB_COLLECTION_USERS]

    def persist_user(self, user):
        if 'username' not in user:
            user['username'] = Helper.make_id()
        user['_id'] = user['username']
        insert_one_result = self._user_collection().insert_one(user)
        return insert_one_result.inserted_id

    def get_users(self):
        return list(self._user_collection().find())
        
    def get_user(self, id):
        return list(self._user_collection().find(id))