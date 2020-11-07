import csv
import re

def url_length(url):
        return len(url)
        
    #...........Returning URL keyword count........
def Keywords(url):
        words = re.findall("(script)|(alert)|(cookie)|(onclick)|(fromCharCode)|(eval)|(iframe)|(src)|(style)|(onload)|(prompt)|(javascript)" , url,re.IGNORECASE)   
        return len(words) 

    #...........Returning encoded char count.........
def Encoded(url):
        words = re.findall("%3c|%3e|%20",url,re.IGNORECASE)
        return len(words)

    #.........Returning count of spcl char............
def Spcl_char(url):
        spcl = re.findall("(<)|(>)|(/)|(=)",url)
        return len(spcl)

    #.........Return the number of domains..........
def Domain(url):
        dom = re.findall('.com',url)
        return len(dom)

    #.........Create feature set...............
def Create_features(url):
        features = [url_length(url),Keywords(url),Encoded(url),Spcl_char(url),Domain(url)]
        return features
def create_class(data,xss):
        label =0
        features = Create_features(data)
        if xss:
            label = 1
        else:
            label= 0
        return features,label

f = open('extra/xssed.txt','r')

with open('xssed3.csv','w') as cs_fp:
        wrt = csv.writer(cs_fp)
        wrt.writerow(['url_length','Keywords','spcl_char','Label'])
        
        for line in f.readlines():
        #print(line)
            feat,l = create_class(line,1)
            #feat.append(l)
            feat = map(str,feat)
            wrt.writerow(feat)

'''
f = open('extra/non_xss.txt','r')

with open('non_xss3.csv','w') as cs_fp:
        wrt = csv.writer(cs_fp)
        wrt.writerow(['url_length','Keywords','spcl_char','Label'])
        
        for line in f.readlines():
        #print(line)
            feat,l = create_class(line,0)
            #feat.append(l)
            feat = map(str,feat)
            wrt.writerow(feat)

'''