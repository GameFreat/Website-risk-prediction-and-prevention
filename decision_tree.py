import treelib
from data_split import *

attributes = ['url_length', 'Keywords', 'Url_count', 'spcl_char', 'Label']


class Data:

    # .............Returns the Unique value in the dataset..........
    def get_unique_val(self, row, col):
        return set([r[col] for r in row])

    # .........Counts no of type of data in dataset.......
    def count_Class(self, row):

        count = {}
        for r in row:

            attribute = r[-1]
            # if attribute ==0 or attribute ==1:
            if attribute not in count:
                count[attribute] = 0

            count[attribute] += 1

        return count

    # ........Class Partitions the Dataset.........
    def partition(self, rows, qtn):

        t_row, f_row = [], []
        for r in rows:

            if qtn.comp(r):
                t_row.append(r)
            else:
                f_row.append(r)

        return t_row, f_row


# ...................Class defines the rules in the node...........

class Node_Rules:
    # ............for numeric data..............
    def __init__(self, col, val):
        self.col = col
        self.val = val

    def comp(self, row):
        values = row[self.col]
        return values >= self.val

    def __repr__(self):
        contn = '>='
        return "Is %s %s %s?" % (attributes[self.col], contn, str(self.val))


class Calculate:
    # ...........navaneetha............
    # .............Calculates Gini Impurity.................
    def gini_idx(self, rows):
        d = Data()
        count = d.count_Class(rows)
        impurity = 1
        for target in count:
            prob = count[target] / float(len(rows))
            impurity -= prob ** 2

        return impurity

    # ..........navaneetha............
    # ...........Calculates Information-gain............
    def information_gain(self, left_set, right_set, uncertainity):

        total_length = len(left_set) + len(right_set)
        prob = float(len(left_set)) / total_length
        gain = uncertainity - prob * \
               self.gini_idx(left_set) - (1 - prob) * self.gini_idx(right_set)

        return gain

        # .............need to push..................

    def find_best_split(self, rows):

        d = Data()
        best_gain = 0
        best_question = None  # keep train of the feature / value that produced it
        current_uncertainty = self.gini_idx(rows)
        n_features = len(rows[0]) - 1  # number of columns

        for col in range(n_features):  # for each feature

            # unique values in the column
            values = set([row[col] for row in rows])

            for val in values:  # for each value

                question = Node_Rules(col, val)

                # try splitting the dataset
                true_rows, false_rows = d.partition(rows, question)

                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                # Calculate the information gain from this split
                gain = self.information_gain(
                    true_rows, false_rows, current_uncertainty)

                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question


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


t = DecisionTree()
tree = treelib.Tree()
my_tree = t.build_tree(training_data, tree, '')
