import numpy as np
import pickle as c
from sklearn.model_selection import train_test_split
from feature_extraction import ExtractFeatures
from naivebayes import NaiveBayes


class TrainTest:
    def accuracy(self,y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy
    
    def save_model(self,nb, name):
        with open(name, 'wb') as fp:
            c.dump(nb, fp)
        print ("Model saved")
    
    

features = []
labels = []
extractor = ExtractFeatures()
(f, l) = extractor.check_dataset("./DesignProject/bad-xss-20000.txt",1)
features += f
labels += l

(f, l) = extractor.check_dataset("./DesignProject/good-xss-20000.txt",0)
features += f
labels += l

features = np.array(features)
labels = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=123)

nb = NaiveBayes()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)

test = TrainTest()
print("Accuracy :", test.accuracy(y_test, predictions))

test.save_model(nb,"./DesignProject/NaiveBayes-model.mdl")




