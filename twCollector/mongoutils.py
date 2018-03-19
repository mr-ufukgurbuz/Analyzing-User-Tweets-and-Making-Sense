#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo, os

# "mLab" Remote Database URI
DBPATH = os.environ['MONGODB_URI']
db_name = 'data-science-database'
collection_name= 'Tweets'


class MongodbClient:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(DBPATH, connectTimeoutMS=30000,
                                                        socketTimeoutMS=None,
                                                        socketKeepAlive=True,
                                                        connect=False)
        self.db = self.mongo_client[db_name]
        self.collection = self.db[collection_name]


class MongodbWriter(MongodbClient):
    def __init__(self, tweets_generator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tweets_generator = tweets_generator

    def __iter__(self):
        count=0;
        for tweet in self.tweets_generator:
            self.collection.insert_one(tweet)
            count+=1
        return count;

    def saveTokenize(self,username):
        count=0;
        for tweet,pure in self.tweets_generator:
            selected_tweets = filter(lambda x: x not in ["RT","https","co","t","ve","in","e"], tweet) #todo Caneeer şunu regex yapda aksin buralar

            tw = {
                "username": username,
                'done': 0,
                "tweet":pure,
                'wordsoftweets': dict((t, 0) for t in list(selected_tweets)),
                }
            self.collection.insert_one(tw)
            count+=1
        return count;

class MongodbReader(MongodbClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for doc in self.collection.find():
            yield doc

    def getOneItem(self,filter={"done":0}):
        return  self.collection.find_one(filter)

    def updateOneItem(self,id,_labeed):

        result = self.collection.update(
            {"_id": id},
            {
                '$set': {
                    'done': 1,
                    'wordsoftweets':_labeed
                }
            }
        )
        return result
