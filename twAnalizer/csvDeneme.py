#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def readFromCSV(filePath):
    documentList = []
    counter = 0
    with open(filePath, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            rowList = [str(counter), row[1]]
            documentList.append(rowList)
            counter += 1
    return documentList

def writeToCSV(filePath, data):
    with open(filePath, "w", newline='', encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    documentList = readFromCSV('C:/Users/_UFUK_/Desktop/document.csv')
    #print(documentList)
    #for doc in documentList:
    #    print(doc)

    writeToCSV('C:/Users/_UFUK_/Desktop/new_document.csv', documentList)

