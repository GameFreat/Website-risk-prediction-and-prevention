from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle as c
from make_dict import make_Dict
from make_dataset import make_Dataset

def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")


a = make_Dict()
d = a.dict()
b = make_Dataset(d)
features, labels = b.datas()
# features, labels = make_dataset(d)

#print (len(features), len(labels))

x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)     #training

preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))
save(clf, "text-classifier.mdl")     #storing trained file


    

