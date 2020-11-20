import re
import csv

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
            with open(data)as f:
                for url in f:
                    features.append(self.Create_features(url))
                    #labelling the dataset 
                    if xss:
                        labels.append(1)
                    else:
                        labels.append(0)
            return features,labels
    
#....................done.......................

class Text_to_csv:

    def txttocsv(self):

        fe= Features()
        f1 = open('xssed.txt','r')


        with open('xssed.csv','w') as cs_fp:
                        wrt = csv.writer(cs_fp)
                        wrt.writerow(['url_length', 'Keywords','url_count' ,'spcl_char', 'Label'])
                        
                        for line in f1.readlines():
                        #print(line)
                            feat,l = fe.create_class(line,1)
                            #feat.append(l)
                            feat = map(str,feat)
                            wrt.writerow(feat)
                        
                    

        f = open('non_xss.txt','r')

        with open('non_xss.csv','w') as cs_fp:
                        wrt = csv.writer(cs_fp)
                        wrt.writerow(['url_length', 'Keywords','url_count' ,'spcl_char', 'Label'])
                        
                        for line in f.readlines():
                        #print(line)
                            feat,l = feat.create_class(line,0)
                            #feat.append(l)
                            feat = map(str,feat)
                            wrt.writerow(feat)


