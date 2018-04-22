#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient
import csv

DBPATH = "mongodb://userName:password@bla_bla_bla_bla/data-science-database"
db_name = 'data-science-database'
collection_name= 'Tweets'

client = MongoClient(DBPATH, connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False)
db = client[db_name]
collection = db[collection_name]
collectionList = collection.find().sort('_id')

classDict = {"Trash":1, "Event/Activity":2, "Name":3, "Address":4, "Date":5, "Company":6, "Age":7, "Job":8, "Place":9, "Contact":10, "ID":11}


def readFromCSV(filePath):
    documentList = []
    with open(filePath, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            documentList.append(row)
    return documentList

def writeToCSV(filePath, data):
    with open(filePath, "w", newline='', encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            writer.writerow(row)

def tokenizer(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenList = tokenizer.tokenize(text)
    return tokenList



if __name__ == '__main__':

    documentList = readFromCSV('C:/Users/_UFUK_/Desktop/document.csv')
    newDocumentList = []

    for doc in documentList:
        doc_id = doc[0]
        text = doc[1]
        tokenList = tokenizer(text)
        #print(tokenList)
        filteredTokenList = filter(lambda x: x not in ["RT", "https", "co", "t", "ve", "in", "e"], tokenList)

        if doc_id != "doc_id":
            currentTweet = collectionList[int(doc_id) - 1]
        token_id = 1

        for token_text in filteredTokenList:
            if doc_id=="doc_id":
                newDocumentList.append([doc_id, "token_id", token_text, "c_id", "c_name"])
            else:
                if currentTweet['done'] == 1:
                    className = currentTweet['wordsoftweets'][token_text]
                    if className != 0:
                        newDocumentList.append([doc_id, token_id, token_text, classDict[className], className])
            token_id += 1

    #print(newDocumentList)
    writeToCSV('C:/Users/_UFUK_/Desktop/documentToken.csv', newDocumentList)


    #print(collection.find().sort('_id')[int("2")-1]['done'])
    #print(collection.find().sort('_id')[1]['wordsoftweets'])
    #print(collection.find().sort('_id')[2]['wordsoftweets'])