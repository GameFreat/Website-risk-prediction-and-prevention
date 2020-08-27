import _pickle as c
import os
import sys
from sklearn import *
from make_dict import make_Dict

class detector:
    def load(self,clf_file):
        with open(clf_file, 'rb') as fp:
            clf = c.load(fp)
        return clf
    def __init__(self):
        clf = self.load("text-classifier.mdl")
        a = make_Dict()
        d = a.dict()
    
        arg = sys.argv[1]
        f = open(arg, 'r')
        features = []
        words = f.read().split(' ')
        for word in d:
                features.append(words.count(word[0]))     #taking count of each word in dictionary present in input
        res = clf.predict([features])     #prediction
        print (["Not Spam", "Spam!"][res[0]])
a = detector()

