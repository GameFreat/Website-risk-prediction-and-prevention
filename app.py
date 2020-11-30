from flask import Flask, render_template, request
import re
import _pickle as c
from testing import Testing

with open("rules.mdl", 'rb') as fp:
    rules = c.load(fp)


class Features():
    # ...........Returning URL Length...........
    def url_length(self, url):
        return len(url)

    # ...........Returning URL keyword count........
    def Keywords(self, url):
        words = re.findall(
            "(alert)|(script)|(%3c)|(%3e)|(%20)|(onclick)|(onerror)|(onload)|(eval)|(src)|(prompt)|(iframe)|(style)", url, re.IGNORECASE)
        return len(words)

    def url_count(self, url):
        if re.search('(http://)|(https://)', url, re.IGNORECASE):
            return 1
        else:
            return 0

    # .........Returning count of spcl char............
    def Spcl_char(self, url):
        spcl = re.findall("(<)|(>)|(/)|(=)", url)
        return len(spcl)

    # .........Create feature set...............
    def Create_features(self, url):
        features = [self.url_length(url), self.Keywords(
            url), self.url_count(url), self.Spcl_char(url)]
        return features


def prediction(sum):
    url = sum
    f = Features()
    features = f.Create_features(url)
    # print(features)
    test = Testing()
    r = test.Test(rules, features)
    label = eval(r[-1])
    d = dict(label)
    for key in d.keys():

        if(key == '0'):
            return("You are safe!This website is not vulnerable to XSS attack")
        else:
            return("Alert!This website is vulnerable to XSS attack")


app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send(value=sum):
    num = request.form['num1']
    sum = chr(num)
    sum = prediction(sum)
    return render_template('index.html', value=sum)


if __name__ == ' __main__':
    app.debug = True
    app.run()
