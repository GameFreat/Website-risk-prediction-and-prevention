import os
from collections import Counter
class make_Dict:
    def dict(self):
        direc = "emails/"
        files = os.listdir(direc)

        emails = [direc + email for email in files]

        words = []
        c = len(emails)     #counting total number of emails

        for email in emails:
            f = open(email, encoding="latin-1")     #opening each mail
            blob = f.read()
            words += blob.split(" ")     #splitting each word
            print (c)
            c -= 1

        for i in range(len(words)):
            if not words[i].isalpha():
                words[i]  = ""     #deleting non alpha words

        dictionary = Counter(words)     #function to count each word in dictionary
        del dictionary[""]     #deletion of empty spaces
        return (dictionary.most_common(3000))
