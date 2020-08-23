import _pickle as c
import os
import sys
from sklearn import *
from collections import Counter


def load(clf_file):
    with open(clf_file, 'rb') as fp:
        clf = c.load(fp)
    return clf

def make_dict():
    direc = "emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files]

    words = []
    c = len(emails)     #counting total number of emails

    for email in emails:
        f = open(email, encoding="latin-1")     #opening each mail
        blob = f.read()
        words += blob.split(" ")     #splitting each word
        print (c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i]  = ""     #deleting non alpha words

    dictionary = Counter(words)     #function to count each word in dictionary
    del dictionary[""]     #deletion of empty spaces
    return (dictionary.most_common(3000))


clf = load("text-classifier.mdl")
d = make_dict()


arg = sys.argv[1]
f = open(arg, 'r')
features = []
words = f.read().split(' ')
for word in d:
        features.append(words.count(word[0]))     #taking count of each word in dictionary present in input
res = clf.predict([features])     #prediction
print (["Not Spam", "Spam!"][res[0]])




