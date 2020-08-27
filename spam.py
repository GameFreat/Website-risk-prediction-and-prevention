import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle as c
from make_dict import make_Dict

def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files]

    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        f = open(email, encoding="latin-1")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))     #taking count of each word in dictionary present in email
        feature_set.append(data)       #storing data list
        if "ham" in email:
            labels.append(0)     #label not spam
        if "spam" in email:
            labels.append(1)     #label spam
        print (c)
        c -= 1
    return feature_set, labels

def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")


a = make_Dict()
d = a.dict()
features, labels = make_dataset(d)

#print (len(features), len(labels))

x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)     #training

preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))
save(clf, "text-classifier.mdl")     #storing trained file


    

