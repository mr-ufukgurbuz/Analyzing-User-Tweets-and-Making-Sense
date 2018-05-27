#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import statistics
from collections import Counter

Document = pd.read_excel('xlsx/document.xlsx')                       # Read 'document.xlsx' file
_textList = Document["text"]
textList = []
textCharNumList = []

Document_Token = pd.read_excel('xlsx/documentToken2.xlsx')           # Read 'documentToken.xlsx' file
tokenTextList = Document_Token[["token_text", "c_name"]]

tokenCharNumList = []

numOfInsLessThanFiveChars = 0
for text in _textList:
    textList.append(str(text))
    textCharNumList.append(len(str(text)))

for tokenText in tokenTextList["token_text"]:
    charCount = len(str(tokenText))
    tokenCharNumList.append(charCount)
    if charCount<5:
        numOfInsLessThanFiveChars += 1


#-------------- "1-a" -------------------
def _1a():
    totalInsNumberOfDataset = len(textList)
    print("a. total number of instances:", totalInsNumberOfDataset)

#-------------- "1-b" -------------------
def _1b():
    avgLengthOfInstance = statistics.mean(textCharNumList)
    print("\nb. average length of instances in characters:", avgLengthOfInstance)

#-------------- "1-c" -------------------
def _1c():
    stdDevOfInstance = statistics.stdev(textCharNumList)
    print("\nc. std dev of length of instances in characters:", stdDevOfInstance)

#-------------- "1-d" -------------------
def _1d():
    avgLengthOfInstance = statistics.mean(tokenCharNumList)
    print("\nd. average length of instances in words (after tokenization):", avgLengthOfInstance)

#-------------- "1-e" -------------------
def _1e():
    stdDevOfInstance = statistics.stdev(tokenCharNumList)
    print("\ne. std dev of length of instances in words (after tokenization):", stdDevOfInstance)

#-------------- "1-f" -------------------
def _1f():
    result10 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(10), columns=['Word', 'Frequency'])
    print("\nf. the most frequent 10 words:")
    print(result10)

    result10 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(10), columns=['Word', 'Frequency']).set_index("Word")
    graph = result10.plot(kind='bar', title ="The most frequent 10 words", legend=True, fontsize=8)
    graph.set_xlabel("Word", fontsize=9)
    graph.set_ylabel("Frequency", fontsize=9)
    plt.plot()

#-------------- "1-g" -------------------
def _1g():
    result50 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(50), columns=['Word', 'Frequency'])
    print("\ng. the most frequent 50 words:")
    print(result50)

    result50 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(50), columns=['Word', 'Frequency']).set_index("Word")
    graph = result50.plot(kind='bar', title ="The most frequent 50 words", legend=True, fontsize=8)
    graph.set_xlabel("Word", fontsize=9)
    graph.set_ylabel("Frequency", fontsize=9)
    plt.plot()

#-------------- "1-h" -------------------
def _1h():
    print("\nh. number of instances that are less than 5 characters:", numOfInsLessThanFiveChars, "\n\n")

# //////////////////////////////////////////////////////////////////

#-------------- "2-a" -------------------
classCountDict = {"trashCount"  :0, "eventCount":0, "nameCount" :0, "addressCount":0, "dateCount":0, "compCount":0,
                  "ageCount"    :0, "jobCount"  :0, "placeCount":0, "contactCount":0, "idCount":0}

classCharNumDict = {"trashCharNumList"  :[0,0], "eventCharNumList" :[0,0], "nameCharNumList"  :[0,0], "addressCharNumList":[0,0], "dateCharNumList" :[0,0], "compCharNumList":[0,0],
                    "ageCharNumList"    :[0,0], "jobCharNumList"   :[0,0], "placeCharNumList" :[0,0], "contactCharNumList":[0,0], "idCharNumList"   :[0,0]}

classDict       = {"Trash":[], "Event":[], "Name":[], "Address":[], "Date":[], "Comp":[], "Age":[], "Job":[], "Place":[], "Contact":[], "ID":[]}


# Number of Class that Less Than Five Characters
trashNumLessThanFiveChars, eventNumLessThanFiveChars, nameNumLessThanFiveChars, addressNumLessThanFiveChars, dateNumLessThanFiveChars, compNumLessThanFiveChars, \
ageNumLessThanFiveChars, jobNumLessThanFiveChars, placeNumLessThanFiveChars, contactNumLessThanFiveChars, idNumLessThanFiveChars = 0,0,0,0,0,0,0,0,0,0,0


searchIndex=0
for c_name in tokenTextList["c_name"]:

    if c_name == "Trash":
        classCountDict["trashCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        trashCharCount = len(str(tokenText))
        classCharNumDict["trashCharNumList"].append(trashCharCount)
        classDict["Trash"].append(tokenText)
        if trashCharCount<5:
            trashNumLessThanFiveChars += 1

    elif c_name == "Event/Activity":
        classCountDict["eventCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        eventCharCount = len(str(tokenText))
        classCharNumDict["eventCharNumList"].append(eventCharCount)
        classDict["Event"].append(tokenText)
        if eventCharCount<5:
            eventNumLessThanFiveChars += 1

    elif c_name == "Name":
        classCountDict["nameCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        nameCharCount = len(str(tokenText))
        classCharNumDict["nameCharNumList"].append(nameCharCount)
        classDict["Name"].append(tokenText)
        if nameCharCount<5:
            nameNumLessThanFiveChars += 1

    elif c_name == "Address":
        classCountDict["addressCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        addressCharCount = len(str(tokenText))
        classCharNumDict["addressCharNumList"].append(addressCharCount)
        classDict["Address"].append(tokenText)
        if addressCharCount<5:
            addressNumLessThanFiveChars += 1

    elif c_name == "Date":
        classCountDict["dateCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        dateCharCount = len(str(tokenText))
        classCharNumDict["dateCharNumList"].append(dateCharCount)
        classDict["Date"].append(tokenText)
        if dateCharCount<5:
            dateNumLessThanFiveChars += 1

    elif c_name == "Company":
        classCountDict["compCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        compCharCount = len(str(tokenText))
        classCharNumDict["compCharNumList"].append(compCharCount)
        classDict["Comp"].append(tokenText)
        if compCharCount<5:
            compNumLessThanFiveChars += 1

    elif c_name == "Age":
        classCountDict["ageCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        ageCharCount = len(str(tokenText))
        classCharNumDict["ageCharNumList"].append(ageCharCount)
        classDict["Age"].append(tokenText)
        if ageCharCount<5:
            ageNumLessThanFiveChars += 1

    elif c_name == "Job":
        classCountDict["jobCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        jobCharCount = len(str(tokenText))
        classCharNumDict["jobCharNumList"].append(jobCharCount)
        classDict["Job"].append(tokenText)
        if jobCharCount<5:
            jobNumLessThanFiveChars += 1

    elif c_name == "Place":
        classCountDict["placeCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        placeCharCount = len(str(tokenText))
        classCharNumDict["placeCharNumList"].append(placeCharCount)
        classDict["Place"].append(tokenText)
        if placeCharCount<5:
            placeNumLessThanFiveChars += 1

    elif c_name == "Contact":
        classCountDict["contactCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        contactCharCount = len(str(tokenText))
        classCharNumDict["contactCharNumList"].append(contactCharCount)
        classDict["Contact"].append(tokenText)
        if contactCharCount<5:
            contactNumLessThanFiveChars += 1

    elif c_name == "ID":
        classCountDict["idCount"] += 1
        tokenText = tokenTextList["token_text"][searchIndex]
        idCharCount = len(str(tokenText))
        classCharNumDict["idCharNumList"].append(idCharCount)
        classDict["ID"].append(tokenText)
        if idCharCount<5:
            idNumLessThanFiveChars += 1

    searchIndex +=1


def _2a():
    print("a. total number of instances:\n", classCountDict)

    df = pd.DataFrame(classCountDict, index=[0])
    graph = df.plot(kind='bar', title ="Total number of instances for classes", legend=True, fontsize=8)
    graph.set_xlabel("Classes", fontsize=12)
    graph.set_ylabel("# of instances", fontsize=12)
    plt.plot()

#-------------- "2-b" -------------------
avgLengthOfClassDict = {"avgLengthOfTrash":0, "avgLengthOfEvent":0, "avgLengthOfName":0, "avgLengthOfAddress":0, "avgLengthOfDate":0, "avgLengthOfComp":0,
                        "avgLengthOfAge":0, "avgLengthOfJob":0, "avgLengthOfPlace":0, "avgLengthOfContact":0, "avgLengthOfID":0}

avgLengthOfClassDict["avgLengthOfTrash"]    = statistics.mean(classCharNumDict["trashCharNumList"])
avgLengthOfClassDict["avgLengthOfEvent"]    = statistics.mean(classCharNumDict["eventCharNumList"])
avgLengthOfClassDict["avgLengthOfName"]     = statistics.mean(classCharNumDict["nameCharNumList"])
avgLengthOfClassDict["avgLengthOfAddress"]  = statistics.mean(classCharNumDict["addressCharNumList"])
avgLengthOfClassDict["avgLengthOfDate"]     = statistics.mean(classCharNumDict["dateCharNumList"])
avgLengthOfClassDict["avgLengthOfComp"]     = statistics.mean(classCharNumDict["compCharNumList"])
avgLengthOfClassDict["avgLengthOfAge"]      = statistics.mean(classCharNumDict["ageCharNumList"])
avgLengthOfClassDict["avgLengthOfJob"]      = statistics.mean(classCharNumDict["jobCharNumList"])
avgLengthOfClassDict["avgLengthOfPlace"]    = statistics.mean(classCharNumDict["placeCharNumList"])
avgLengthOfClassDict["avgLengthOfContact"]  = statistics.mean(classCharNumDict["contactCharNumList"])
avgLengthOfClassDict["avgLengthOfID"]       = statistics.mean(classCharNumDict["idCharNumList"])

def _2b():
    print("\nb. average length of instances in characters:\n", avgLengthOfClassDict)

    df = pd.DataFrame(avgLengthOfClassDict, index=[0])
    graph = df.plot(kind='bar', title ="Average length of instances in characters for classes", legend=True, fontsize=8)
    graph.set_xlabel("Classes", fontsize=12)
    graph.set_ylabel("Average length of instances", fontsize=12)
    plt.plot()

#-------------- "2-c" -------------------
stdDevOfClassDict = {"stdDevOfTrash":0, "stdDevOfEvent":0, "stdDevOfName"   :0, "stdDevOfAddress":0, "stdDevOfDate":0, "stdDevOfComp":0,
                     "stdDevOfAge"  :0, "stdDevOfJob"   :0, "stdDevOfPlace" :0, "stdDevOfContact":0, "stdDevOfID":0}

stdDevOfClassDict["stdDevOfTrash"]    = statistics.stdev(classCharNumDict["trashCharNumList"])
stdDevOfClassDict["stdDevOfEvent"]    = statistics.stdev(classCharNumDict["eventCharNumList"])
stdDevOfClassDict["stdDevOfName"]     = statistics.stdev(classCharNumDict["nameCharNumList"])
stdDevOfClassDict["stdDevOfAddress"]  = statistics.stdev(classCharNumDict["addressCharNumList"])
stdDevOfClassDict["stdDevOfDate"]     = statistics.stdev(classCharNumDict["dateCharNumList"])
stdDevOfClassDict["stdDevOfComp"]     = statistics.stdev(classCharNumDict["compCharNumList"])
stdDevOfClassDict["stdDevOfAge"]      = statistics.stdev(classCharNumDict["ageCharNumList"])
stdDevOfClassDict["stdDevOfJob"]      = statistics.stdev(classCharNumDict["jobCharNumList"])
stdDevOfClassDict["stdDevOfPlace"]    = statistics.stdev(classCharNumDict["placeCharNumList"])
stdDevOfClassDict["stdDevOfContact"]  = statistics.stdev(classCharNumDict["contactCharNumList"])
stdDevOfClassDict["stdDevOfID"]       = statistics.stdev(classCharNumDict["idCharNumList"])

def _2c():
    print("\nc. std dev of length of instances in characters:\n", stdDevOfClassDict)

    df = pd.DataFrame(stdDevOfClassDict, index=[0])
    graph = df.plot(kind='bar', title ="Std dev of length of instances in characters for classes", legend=True, fontsize=8)
    graph.set_xlabel("Classes", fontsize=12)
    graph.set_ylabel("Std dev of length of instances", fontsize=12)
    plt.plot()

#-------------- "2-f" -------------------
classMost10Dict = {"Trash":None, "Event":None, "Name":None, "Address":None, "Date":None, "Comp":None, "Age":None, "Job":None,
                   "Place":None, "Contact":None, "ID":None}

classMost10Dict["Trash"]   = pd.DataFrame(Counter(classDict["Trash"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Event"]   = pd.DataFrame(Counter(classDict["Event"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Name"]    = pd.DataFrame(Counter(classDict["Name"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Address"] = pd.DataFrame(Counter(classDict["Address"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Date"]    = pd.DataFrame(Counter(classDict["Date"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Comp"]    = pd.DataFrame(Counter(classDict["Comp"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Age"]     = pd.DataFrame(Counter(classDict["Age"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Job"]     = pd.DataFrame(Counter(classDict["Job"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Place"]   = pd.DataFrame(Counter(classDict["Place"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["Contact"] = pd.DataFrame(Counter(classDict["Contact"]).most_common(10), columns=['Word', 'Frequency'])
classMost10Dict["ID"]      = pd.DataFrame(Counter(classDict["ID"]).most_common(10), columns=['Word', 'Frequency'])

def _2f():
    print("\nf. the most frequent 10 words:")

    for classMost10Key, classMost10Value in zip(classMost10Dict.keys(), classMost10Dict.values()):
        print("\n------", classMost10Key, "------\n")
        if (len(classMost10Value) != 0):
            print(classMost10Value, "\n")
        else:
            print([None], "\n")


#-------------- "2-g" -------------------
classMost50Dict = {"Trash":None, "Event":None, "Name":None, "Address":None, "Date":None, "Comp":None, "Age":None, "Job":None,
                   "Place":None, "Contact":None, "ID":None}

classMost50Dict["Trash"]   = pd.DataFrame(Counter(classDict["Trash"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Event"]   = pd.DataFrame(Counter(classDict["Event"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Name"]    = pd.DataFrame(Counter(classDict["Name"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Address"] = pd.DataFrame(Counter(classDict["Address"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Date"]    = pd.DataFrame(Counter(classDict["Date"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Comp"]    = pd.DataFrame(Counter(classDict["Comp"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Age"]     = pd.DataFrame(Counter(classDict["Age"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Job"]     = pd.DataFrame(Counter(classDict["Job"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Place"]   = pd.DataFrame(Counter(classDict["Place"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["Contact"] = pd.DataFrame(Counter(classDict["Contact"]).most_common(50), columns=['Word', 'Frequency'])
classMost50Dict["ID"]      = pd.DataFrame(Counter(classDict["ID"]).most_common(50), columns=['Word', 'Frequency'])

def _2g():
    print("\ng. the most frequent 50 words:")

    for classMost50Key, classMost50Value in zip(classMost50Dict.keys(), classMost50Dict.values()):
        print("\n------", classMost50Key, "------\n")
        if (len(classMost50Value) != 0):
            print(classMost50Value, "\n")
        else:
            print([None], "\n")


#-------------- "2-h" -------------------
def _2h():
    print("\nh. number of instances that are less than 5 characters:")

    print("\nTrash Count:\t",       trashNumLessThanFiveChars)
    print("Event Count:\t",         eventNumLessThanFiveChars)
    print("Name Count:\t\t",        nameNumLessThanFiveChars)
    print("Address Count:\t",       addressNumLessThanFiveChars)
    print("Date Count:\t\t",        dateNumLessThanFiveChars)
    print("Comp Count:\t\t",        compNumLessThanFiveChars)
    print("Age Count:\t\t",         ageNumLessThanFiveChars)
    print("Job Count:\t\t",         jobNumLessThanFiveChars)
    print("Place Count:\t",         placeNumLessThanFiveChars)
    print("Contact Count:\t",       contactNumLessThanFiveChars)
    print("ID Count:\t\t",          idNumLessThanFiveChars)


if __name__ == '__main__':
    print("\n\t##### <<< ANSWERS >>> #####\n")

    print("----- (1) For the whole dataset -----")
    _1a()       # a. total number of instances
    _1b()       # b. average length of instances in characters
    _1c()       # c. std dev of length of instances in characters
    _1d()       # d. average length of instances in words (after tokenization)
    _1e()       # e. std dev of length of instances in words (after tokenization)
    _1f()       # f. the most frequent 10 words
    _1g()       # g. the most frequent 50 words
    _1h()       # h. number of instances that are less than 5 characters

    print("----- (2) For each class label -----")
    _2a()       # a. total number of instances
    _2b()       # b. average length of instances in characters
    _2c()       # c. std dev of length of instances in characters
    _2f()       # f. the most frequent 10 words
    _2g()       # g. the most frequent 50 words
    _2h()       # h. number of instances that are less than 5 characters

    #plt.show()
