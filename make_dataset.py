import os
class make_Dataset:
    def __init__(self,dict):
        self.dictionary = dict
    def datas(self):
        direc = "emails/"
        files = os.listdir(direc)

        emails = [direc + email for email in files]

        feature_set = []
        labels = []
        c = len(emails)

        for email in emails:
            data = []
            f = open(email, encoding="latin-1")
            words = f.read().split(' ')
            for entry in self.dictionary:
                data.append(words.count(entry[0]))     #taking count of each word in dictionary present in email
            feature_set.append(data)       #storing data list
            if "ham" in email:
                labels.append(0)     #label not spam
            if "spam" in email:
                labels.append(1)     #label spam
            print (c)
            c -= 1
        return( feature_set, labels)
