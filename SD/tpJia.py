#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:32:28 2016

@author: davidjia
"""

import sklearn as sk
import sklearn.datasets as skd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import fetch_20newsgroups

trainingSet = []
testSet = []
files = []

import codecs

for i in range(1,6):
    #f = open("appleCompany"+str(i)+".txt")
    f = codecs.open("appleCompany"+str(i)+".txt", encoding='utf-8')
    files.append(f.read().encode('utf-8'))
    
for i in range(6,11):
    f = open("appleFruit"+str(i)+".txt")
    files.append(f.read())
f.close()

#return the number of the word apple in text
def numberApple(apple,text):
    number = 0
    for word in text:
        if word == apple:
            number += 1
    return number

  
        

#count_vect = CountVectorizer(stop_words=’english’)
#X_train_counts = count_vect.fit_transform(trainingFiles)

#training=X_train_counts.toarray()


#neigh = KNeighborsClassifier(n_neighbors=k)
#neigh.fit(training,trainingCl)
