import re

class ExtractFeatures:  

    def get_len(self,url):  
        self.url = url
        return len(url)

    def get_special_characters(self,url):
        self.url = url
        return len(re.findall("[<>()%\'\"/]", url, re.IGNORECASE))

    def get_suspicious_numbers(self,url):
        self.url = url
        return len(re.findall("\d", url, re.IGNORECASE))

    def get_bad_code(self,url):
        self.url = url
        return len(re.findall("(alert)|(script)|(document.cookie)|(document.location)|(%3c)|(%3e)|(%20)|(onclick)|(onerror)|(onload)|(eval)|(src)|(prompt)|(iframe)|(style)",url,re.IGNORECASE))

    def get_features(self,url):
        self.url = url
        return [self.get_special_characters(url), self.get_suspicious_numbers(url),self.get_bad_code(url), self.get_len(url)]

    def check_dataset(self, filename, is_xss):
        features=[]
        labels=[]
        with open(filename) as file:
            for line in file:
                features.append(self.get_features(line))
                labels.append(is_xss)

        return(features, labels)

