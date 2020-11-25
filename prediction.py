import re
import _pickle as c
from testing import Testing
#from feature_extraction import Features

with open("rules.mdl", 'rb') as fp:
    rules = c.load(fp)


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


url = input('Enter the website URL : ')
f = Features()
features = f.Create_features(url)
#print(features)
test = Testing()
r = test.Test(rules,features)
label = eval(r[-1])
d = dict(label)
#print(d.keys())

for key in d.keys() :
    
    if(key == '0'):
        print("\nYou are safe!This website is not vulnerable to XSS attack\n")
    else:
        print("\nAlert!This website is vulnerable to XSS attack\n")