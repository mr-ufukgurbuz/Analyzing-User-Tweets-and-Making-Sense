#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from twCollector.tweetcollector import TwitterAPI
from twCollector.tweettokenizer import TwitterTokenizer
from twCollector.mongoutils import *
import time

consumer_key = 'FnrpmIW63z6fFLs4YomM6IdCD'
consumer_secret = 'LQR2ChhZuJeRiwkyqzqYRLxhgnKYonYq3BChLYQOwyoekSAOJj'
access_token = '356930017-jupA3DwrcIfDdDev0Bfj38KO6oM4xmI1LN1pcpEW'
access_token_secret = 'Z73L0vrIvW7s49yKmdNATMvPg6IkpVgp64BbmdQ6mobPh'

def collectTweet(userlist):

    tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    start_time = time.time();
    endTime=time.time();
    total=0
    for uname in userlist:

        user_tweet_generator = tw.get_user_tweets(uname)
        tokenized_tweet_generator = TwitterTokenizer(user_tweet_generator)

        mdb_writer = MongodbWriter(tokenized_tweet_generator)
        _count=mdb_writer.saveTokenize(uname);

        print("{} 's {} numbers tweets added in seconds {}".format(uname,_count,int(time.time()-endTime)))
        endTime = time.time();
        total=total+int(_count)


    print("{} users , {} tweets , in  {} seconds".format(len(userlist),total,int(time.time()-start_time)))

def main():

    with open("userlist.txt") as f:
        content = f.readlines()
    userList=[x.strip() for x in content]
    print(userList);
    collectTweet(userList)



main()