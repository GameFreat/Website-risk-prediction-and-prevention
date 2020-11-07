# .............program to build tree(NAVANEETHA).....................
import csv
import treelib

training_data = []

with open("test_Set.csv") as tsv:
    for line in csv.reader(tsv, delimiter=","):
        training_data.append(list(line))

attributes = ['url_length', 'Keywords', 'Encoded', 'spcl_char', 'Domain', 'Label']


# .............Returns the Unique value in the dataset..........
def get_unique_val(row, col):
    return set([r[col] for r in row])


# .........COunts no of type of data in dataset.......
def count_Class(row):
    count = {}
    for r in row:

        attribute = r[-1]
        if attribute not in count:
            count[attribute] = 0

        count[attribute] += 1
    return count


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


def partition(rows, qtn):
    t_row, f_row = [], []
    for r in rows:

        if qtn.comp(r):
            t_row.append(r)
        else:
            f_row.append(r)

    return t_row, f_row


class Calculate:
    # ...........navaneetha............
    # .............Calculates Gini Impurity.................
    def gini_idx(self, rows):
        count = count_Class(rows)
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
        gain = uncertainity - prob * self.gini_idx(left_set) - (1 - prob) * self.gini_idx(right_set)

        return gain

        # .............need to push..................

    def find_best_split(self, rows):

        best_gain = 0
        best_question = None  # keep train of the feature / value that produced it
        current_uncertainty = self.gini_idx(rows)
        n_features = len(rows[0]) - 1  # number of columns

        for col in range(n_features):  # for each feature

            values = set([row[col] for row in rows])  # unique values in the column

            for val in values:  # for each value

                question = Node_Rules(col, val)

                # try splitting the dataset
                true_rows, false_rows = partition(rows, question)

                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                # Calculate the information gain from this split
                gain = self.information_gain(true_rows, false_rows, current_uncertainty)

                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question


class Leaf:

    def __init__(self, rows):
        self.predictions = count_Class(rows)


# ................Asks a question...................
class Node:
    # This holds a reference to the question, and to the two child nodes.

    def __init__(self, rule, right_node, left_node):
        self.rule = rule
        self.right_node = right_node
        self.left_node = left_node


# ................Midhul...................
class DecisionTree:

    def _init_(self):
        self.arr = []

    def build_tree(self, dataset, tree, par):

        cal = Calculate()
        gain, question = cal.find_best_split(dataset)

        # .......Checking for leaf node.......
        if gain == 0:
            return Leaf(dataset)

        self.arr.append(question)
        if tree.root == None:

            par = question

            tree.create_node(question, par)
            right, left = partition(dataset, question)
            right_branch = self.build_tree(right, tree, par)
            left_branch = self.build_tree(left, tree, par)
        else:

            if question in arr:
                ID = question + '1'
                tree.create_node(question, ID, parent=par)
                par = ID

            else:
                tree.create_node(question, question, parent=par)
                par = question

            right, left = partition(dataset, question)
            right_branch = self.build_tree(right, tree, par)
            left_branch = self.build_tree(left, tree, par)

        return tree


t = DecisionTree()
tree = treelib.Tree()
arr = []
my_tree = t.build_tree(training_data, tree, '')
# tree.show()
print(tree.leaves())
print(tree.paths_to_leaves())