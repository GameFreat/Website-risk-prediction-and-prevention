import re


class Features():
    # ...........Returning URL Length...........
    def url_length(self, url):
        return len(url)

    # ...........Returning URL keyword count........
    def Keywords(self, url):
        words = re.findall(
            "(script)|(alert)|(cookie)|(onclick)|(fromCharCode)|(eval)|(iframe)|(src)|(style)|(onload)|(prompt)|("
            "javascript)",
            url, re.IGNORECASE)
        return len(words)

        # ...........Returning encoded char count.........

    def Encoded(self, url):
        words = re.findall("%3c|%3e|%20", url, re.IGNORECASE)
        return len(words)

    # .........Returning count of spcl char............
    def Spcl_char(self, url):
        spcl = re.findall("(<)|(>)|(/)|(=)", url)
        return len(spcl)

    # .........Create feature set...............
    def Create_features(self, url):
        features = [self.url_length(url), self.Keywords(url), self.Encoded(url), self.Spcl_char(url)]
        return features