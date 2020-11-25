import re
import csv
import random

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
        
    def create_class(self,data,xss):
            labels = []
            features=[]
            #with open(data)as f:
            #for url in f:
            features.append(self.Create_features(data))
                #labelling the dataset 
            if xss:
                        features.append(1)
            else:
                        features.append(0)
            return features#,labels
    
#....................done.......................
data=[]
class txtto_list:
    def List(self):
        
        fe= Features()
        file = open('xssed.txt','r')
        for f in file:
            #l1=[]
            feat=fe.Create_features(f)
            #l1.append(feat)
            feat.append(1)
            data.append(feat)
        
        file = open('non_xss.txt','r')
        for f in file:
            #l1=[]
            feat=fe.Create_features(f)
            #l1.append(feat)
            feat.append(0)
            data.append(feat)

        random.shuffle(data)
        with open('xssed.csv','w') as cs_fp:
            wrt = csv.writer(cs_fp)
            for line in data:
                #line=map(str,line)
                wrt.writerow(line)

t = txtto_list()
t.List()
