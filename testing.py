from data_split import testing_data
import _pickle as file
# from extract_rules import rules


class Testing:

    def Test(self, rules, data):
        attributes = ['url_length', 'Keywords', 'Url_count', 'spcl_char', 'Label']
        qtn = ''
        split = []
        num = ''
        # node = tree.all_nodes()
        for rule in rules:
            c = 0
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
                    if int(data[pos]) >= val:
                        c += 1
                        continue
                    else:
                        break
                else:
                    if cndtn == '<':
                        if int(data[pos]) < val:
                            c += 1
                            continue
                        else:
                            break

            if c == len(rule) - 1:
                return rule

    def accuracy(self, rules):
        c = 0
        for i in testing_data:
            # print(i)
            lab = self.Test(rules, i)
            label = eval(lab[-1])
            d = dict(label)
            l = str(i[-1])
            if l in d:
                c += 1
        return c


with open("rules.mdl", 'rb') as fp:
    rules = file.load(fp)
test = Testing()
c = test.accuracy(rules)
print('len of test data::', len(testing_data))
print('acc=', c / len(testing_data))
