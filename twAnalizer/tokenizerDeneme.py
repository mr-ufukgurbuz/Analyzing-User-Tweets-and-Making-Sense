#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import RegexpTokenizer

def tokenizer(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenList = tokenizer.tokenize(text)
    return tokenList

if __name__ == '__main__':
    s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."
    tokenList = tokenizer(s)
    print(tokenList)
