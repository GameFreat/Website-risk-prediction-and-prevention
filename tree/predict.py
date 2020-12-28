import re
#import accuracy
from tree import *
import pickle as c

class Features():
    #...........Returning URL Length...........
    def url_length(self,url):
        return len(url)
        
    #...........Returning URL keyword count........
    def Keywords(self,url):
        words = re.findall("(alert)|(script)|(%3c)|(%3e)|(%20)|(onclick)|(onerror)|(onload)|(eval)|(src)|(prompt)|(iframe)|(style)",url,re.IGNORECASE)
        return len(words)

    def url_count(self,url):
        if re.search('(http://)|(https://)', url, re.IGNORECASE) :
            return 1
        else:
            return 0
    
    #.........Returning count of spcl char............
    def Spcl_char(self,url):
        spcl = re.findall("(<)|(>)|(/)|(=)",url)
        return len(spcl)

    #.........Create feature set...............
    def Create_features(self,url):
        features = [self.url_length(url),self.Keywords(url),self.url_count(url),self.Spcl_char(url)]
        return features
        
    
class Output:

    def load(self,clf_file):
        with open(clf_file, 'rb') as fp:
            my_tree = c.load(fp)
        return my_tree

    def Label(self,row, node):
        if isinstance(node, Leaf):
            return node.predictions

        if node.question.match(row):
            return self.Label(row, node.true_branch)
        else:
            return self.Label(row, node.false_branch)

    def result(self,data):
        row=[]
        for i in range(len(data)):
           row.append(str(data[i]))
        #print(type(i))
        #t=accuracy.Test()
        my_tree=self.load("text-classifier.mdl")
        val=self.Label(row,my_tree)
        return val

    def Prediction(self):
        
        url=input('Enter the URL::')
        f=Features()
        feat=f.Create_features(url)
        #print(feat)
        val=self.result(feat)
        #print(val)
        if '1' in val:
            print('Malicious !!!')
        else:
            print('Benign')

o=Output()
o.Prediction()