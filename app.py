#!flask/bin/python

from flask import Flask, jsonify, request, render_template
import  sys, json, time
from bson import json_util
from  twCollector.mongoutils import MongodbReader


app = Flask(__name__, template_folder='template')
PATH=sys.path[0]
item=None;
client = None


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def list():
    global item,client
    client=MongodbReader();
    item=client.getOneItem()

    client.createTweetSessionTimer()                # Starts tweet session timer as '5 minute'

    return  json.dumps(item,default=json_util.default);


@app.route('/previous', methods=['GET'])
def previousTweet():
    global item,client
    client.PREVIOUS_STATUS = True                   # Unlocks current tweet if there is 'previous' operation

    while(client.LOCK_STATUS):                      # If LOCK_STATUS==True, wait for 'unlock' operation;
        time.sleep(0.1)

    item=client.getPreviousItem()                   # Then, continue for 'previous' operation
    return  json.dumps(item,default=json_util.default);


@app.route('/save', methods=['POST'])
def save():
    global item,client
    client.LOCK_STATUS=False                       # Unlocks current tweet if there is 'save' operation before '5 minute'
    data = request.json
    for i in range(0,len(data)):

        item["wordsoftweets"][data[i]["Words"]]=data[i]["Label"]

    result=client.updateOneItem(item["_id"],item["wordsoftweets"])
    if result['updatedExisting']==True:
        return json.dumps({"status":0})
    else:
        return json.dumps({"status": 1})


if __name__ == '__main__':
    app.run(port=5000)
