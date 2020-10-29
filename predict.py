from feature_extraction import Features
import numpy as np
import pickle
class Main:
    
    def getPath(self,url):
        
        self.url = url
        return url.split('/',3)[3]

    def load_mdl(self,dt_file):
        with open(dt_file,'rb') as fp:

            dt = pickle.load(fp)

        return dt

main = Main()
url = input('enter url:')
url_path = main.getPath(url)

dt =main.load_mdl("decision-tree-model.mdl")

features = []
feat = Features
features.append(np.array((feat.get_feature(url_path))))
features = np.array(features)
pred = dt.predict(features)

print(["\nnon-vulnerable to XSS\n","\nVulnerable to XSS!\n"][pred[0]])