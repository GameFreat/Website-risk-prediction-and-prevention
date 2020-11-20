import _pickle as file
import re
from features import Features

with open("rules.mdl", 'rb') as fp:
    rules = file.load(fp)

class Prediction:

    def getPath(self,url):

        self.url = url
        try:
            return url.split('/')[3]
        except:
            return " "

    def predict(self,feature_list):

        attributes = ['url_length', 'Keywords', 'Url_count', 'spcl_char']
        #f = Features()
        #url = input("Enter the url : ")
        #tester = [1023, 70, 87, 66]
        #print(tester)
        for rule in rules:
            c = 0
            tag = rule[len(rule) - 1]
            for r in range(len(rule) - 1):
                qtn = rule[r]
                split = qtn.split()
                question = split[1]
                num = split[-1]
                n = num.translate({ord('?'): None})
                val = int(n)
                for attr in attributes:
                    if attr == question:
                        pos = attributes.index(attr)
                        break

                cndtn = split[2]
                # print(rule)
                # print(data[pos],cndtn,val)
                if cndtn == '>=':
                    if int(feature_list[pos]) >= val:
                        c += 1
                        continue
                    else:
                        break
                else:
                    if cndtn == '<':
                        if int(feature_list[pos]) < val:
                            c += 1
                            continue
                        else:
                            break

            if c == len(rule) - 1:
                print("Rule : ",rule)
                #print(tag[2])

                if tag[2] == '0':
                    print("Not vulnerable")
                else:
                    print("Vulnerable")

url = input("Enter the url : ")
P = Prediction()
url_path = P.getPath(url)
F = Features()
feature_list = F.Create_features(url_path)
P.predict(feature_list)
