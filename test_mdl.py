import numpy as np
import pickle as p
from sklearn.model_selection import train_test_split
from feature_extraction import Features
from Decision_Tree import DecisionTree

class Accuracy:

    #.......Returns Accuracy.......
    def accuracy(self,y_true,y_pred):
        accuracy = np.sum(y_true == y_pred)/len(y_true)
        return accuracy

    def save_mdl(self,dt,name):
        with open(name,'wb') as fp:
            p.dump(dt,fp)

        print('model saved !!')

feature=[]
label =[]

feat = Features()
f,l = feat.create_class('xssed.txt',1)
feature.append(f)
label.append(l)

f,l = feat.create_class('non_xss.txt',0)
feature.append(f)
label.append(l)

feature = np.array(feature)
label = np.array(label)

x_train, x_test, y_train, y_test = train_test_split(feature,label ,test_size=0.2,random_state=1234)

clf = DecisionTree(max_depth=10)
clf.fit(x_train,y_train)
pred = clf.predict(x_test)

tts = Accuracy()
print('Accuracy :',tts.accuracy(y_test,pred))

tts.save_mdl(clf,"decision-tree-model.mdl")