#!flask/bin/python

from flask import Flask, request, render_template, session
from flask_session import Session
import  sys, json, time
from bson import json_util
from  twCollector.mongoutils import MongodbReader

SESSION_TYPE = 'filesystem'

app = Flask(__name__, template_folder='template')
app.config.from_object(__name__)
#app.secret_key = 'any random string'

Session(app)
PATH=sys.path[0]
#item=None;
client = None


@app.route('/', methods=['GET'])
def start():
    global client
    client = MongodbReader();
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def list():
    global client
    item=client.getOneItem()

    session['item']=item
    client.createTweetSessionTimer()                # Starts tweet session timer as '5 minute'

    return  json.dumps(item,default=json_util.default);


@app.route('/previous', methods=['GET'])
def previousTweet():
    global client
    client.PREVIOUS_STATUS = True                   # Unlocks current tweet if there is 'previous' operation

    while(client.LOCK_STATUS):                      # If LOCK_STATUS==True, wait for 'unlock' operation;
        time.sleep(0.1)

    item=client.getPreviousItem()                   # Then, continue for 'previous' operation

    session['item']=item
    return  json.dumps(item,default=json_util.default);


@app.route('/save', methods=['POST'])
def save():
    global client
    item=dict(session['item'])
    client.LOCK_STATUS=False                       # Unlocks current tweet if there is 'save' operation before '5 minute'

    data = request.json
    for i in range(0,len(data)):

        item["wordsoftweets"][data[i]["Words"]]=data[i]["Label"]

    session['item']=item

    result=client.updateOneItem(item["_id"],item["wordsoftweets"])
    if result['updatedExisting']==True:
        return json.dumps({"status":0})
    else:
        return json.dumps({"status": 1})


if __name__ == '__main__':
    app.run(port=5000, threaded=True)
