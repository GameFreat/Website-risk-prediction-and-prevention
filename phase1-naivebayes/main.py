import numpy as np
from feature_extraction import ExtractFeatures 

import pickle as c

class Main:
    def getPath(self,url):
        self.url = url
        try:
            return url.split('/',3)[3]
        except:
            return " "
    
    def load_model(self,nb_file):
        with open(nb_file, 'rb') as fp:
            nb = c.load(fp)
        return nb

main = Main()
url = input("\nEnter your URL : ")
url_path = main.getPath(url)
#print(url_path)

nb = main.load_model("./DesignProject/NaiveBayes-model.mdl")

features = []
extractor = ExtractFeatures()
features.append(np.array((extractor.get_features(url_path))))
features = np.array(features)
prediction = nb.predict(features)
#print(prediction)

print(["\nURL is non-vulnerable to XSS\n","\nAlert!!Vulnerable to XSS!\n"][prediction[0]])

