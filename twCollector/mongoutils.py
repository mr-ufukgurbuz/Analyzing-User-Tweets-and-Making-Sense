#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo, os, _thread, time


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

        self.currentTweetID = None


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
                "tweetID" : username + "-" + str(count),
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
        self.LOCK_STATUS = True

    def __iter__(self):
        for doc in self.collection.find():
            yield doc

    def getOneItem(self,filter={"done":0}):
        self.currentTweetID = self.collection.find_one(filter)["tweetID"]
        #print(self.getPreviousItem())
        return  self.collection.find_one(filter)

    def getPreviousItem(self):
        previousTweetID = self.findPreviousTweetID(self.currentTweetID)
        self.currentTweetID = previousTweetID       # swap "currentTweetID" by "previousTweetID"
        filter = {"tweetID": previousTweetID}
        return self.collection.find_one(filter=filter)

    def findPreviousTweetID(self, currentTweetID):  # @ufukgurbuz44-8
        tweetID = currentTweetID.split("-")
        _id = int(tweetID[1])
        if(_id != 0):
            _id = _id - 1

        previousTweetID = tweetID[0] + "-" + str(_id)
        return previousTweetID

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

    def createTweetSessionTimer(self):
        _thread.start_new_thread(self.startTweetSessionTimer, ("helloNewLockThread",))  # Starts a timer to lock for '5 minute'
        #print("currentTweetID: ", self.currentTweetID)

    def startTweetSessionTimer(self, threadName):
        self.lockCurrentTweet()             # Locks current tweet for multiple pull requests
        startTime = time.time()

        while self.LOCK_STATUS:
            endTime = time.time()
            elapsedTime = int(endTime - startTime) + 1

            #print(self.currentTweetID, " -> timer :", elapsedTime)

            if (elapsedTime % 300) == 0:     # Sets timer as '5 minute'
                self.unlockCurrentTweet()   # Unlocks current tweet if there is no 'save' operation after '1 minute'
                break
            time.sleep(0.5)

    def lockCurrentTweet(self):
        #print("lockTweetID: ", self.currentTweetID)
        result = self.collection.update(
            {"tweetID": self.currentTweetID},
            {
                '$set': {
                    'done':2        # Lock tweet status
                }
            }
        )
        return result

    def unlockCurrentTweet(self):
        #print("unlockTweetID: ", self.currentTweetID)
        result = self.collection.update(
            {"tweetID": self.currentTweetID},
            {
                '$set': {
                    'done':0        # Unlock tweet status
                }
            }
        )
        return result