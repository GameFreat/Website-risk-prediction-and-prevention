import csv
import treelib
import random
class Train_Test:
    def train_test(self,dataset, test_state):
            test_ratio = 100 * test_state
            train_ratio = 100 - test_ratio
            training_set, testing_set = [], []
            # dataset=[]
            c = 0
            len_train = (len(dataset) * train_ratio) / 100
            len_test = len(dataset) - len_train
            random.shuffle(data)
            # .....Splitting the dataset.......
            for i in range(int(len_train)):
                training_set.append(dataset[i])
                c += 1
            print(len_train, c)
            for i in range(int(len_train), len(dataset)):
                testing_set.append(dataset[i])

            return training_set, testing_set


data = []
t=Train_Test()
with open('xssed.csv') as tsv:
    for line in csv.reader(tsv, delimiter=','):
            data.append(list(line))
training_data, testing_data = t.train_test(data, 0.2)
print(len(training_data), len(testing_data))

attributes = ['url_length', 'Keywords','url_count', 'spcl_char', 'Label']

class Leaf:
    
    def __init__(self, rows):
        d = Data()
        self.predictions = d.count_Class(rows)


# ................Asks a question...................


class Decision_Node:
    # This holds a reference to the question, and to the two child nodes.

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


class Counter:
    def __init__(self):
        self.count = 0

    def get_count(self):
        self.count = self.count + 1
        return str(self.count + 1)


class DecisionTree:

    def __init__(self):
        self.arr = []
        self.counter = Counter()

    def build_tree(self, dataset, tree, par):

        cal = Calculate()
        d = Data()
        gain, question = cal.find_best_split(dataset)

        # .......Checking for leaf node.......
        if gain == 0:
            if question in self.arr:
                ID = question + self.counter.get_count()
                tree.create_node(tree.predictions, ID, parent=par)
                par = ID

            else:
                tree.create_node(str(Leaf(dataset).predictions),
                                 self.counter.get_count() + str(question), parent=par)
                par = question
            return tree

        self.arr.append(question)
        # print(self.arr)
        if tree.root == None:

            par = str(question)

            tree.create_node(str(question), par)
            right, left = d.partition(dataset, question)
            right_branch = self.build_tree(right, tree, par)
            left_branch = self.build_tree(left, tree, par)
        else:

            if question in self.arr:
                ID = self.counter.get_count() + str(question)
                tree.create_node(str(question), ID, parent=par)
                par = ID

            else:
                ID = self.counter.get_count() + str(question)
                tree.create_node(str(question), question, parent=par)
                par = question

            right, left = d.partition(dataset, question)
            right_branch = self.build_tree(right, tree, par)
            left_branch = self.build_tree(left, tree, par)

        # return tree
        return Decision_Node(question, right, left)



