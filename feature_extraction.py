import re

class Features():
    #...........Returning URL Length...........
    def url_length(self,url):
        return len(url)
        
    #...........Returning URL keyword count........
    def Keywords(self,url):
        words = re.findall("(script)|(alert)|(cookie)|(onclick)|(fromCharCode)|(eval)|(iframe)|(src)|(style)|(onload)|(prompt)|(javascript)" , url,re.IGNORECASE)   
        return len(words) 

    #...........Returning encoded char count.........
    def Encoded(self,url):
        words = re.findall("%3c|%3e|%20",url,re.IGNORECASE)
        return len(words)

    #.........Returning count of spcl char............
    def Spcl_char(self,url):
        spcl = re.findall("(<)|(>)|(/)|(=)",url)
        return len(spcl)

    #.........Return the number of domains..........
    def Domain(self , url):
        dom = re.findall('.com',url)
        return len(dom)

    #.........Create feature set...............
    def Create_features(self,url):
        features = [self.url_length(url),self.Keywords(url),self.Encoded(url),self.Spcl_char(url),self.Domain(url)]
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


