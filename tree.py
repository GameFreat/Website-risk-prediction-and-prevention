#...............PROGRAM TO BUILD AND PRINT DECISION TREES.............
import csv
attributes = ['url_length','Keywords','Encoded','spcl_char','Domain','Label']

training_data = []
testing_data = []

with open("test_Set.csv") as tsv:
    for line in csv.reader(tsv, delimiter=","):
                
        testing_data.append(list(line))

with open("xss.csv") as tsv:
            for line in csv.reader(tsv, delimiter=","):
                
                training_data.append(list(line))

def unique_vals(rows, col):
    #Find the unique values for a column in a dataset
    return set([row[col] for row in rows])


def class_counts(rows):
    #Counts the number of each type of example in a dataset
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

#class_counts(training_data)

def is_numeric(value):
    #Test if a value is numeric.
    return isinstance(value, int) or isinstance(value, float)

is_numeric(7)

class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            attributes[self.column], condition, str(self.value))

def partition(rows, question):
    
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

class Calculate:

    def gini(self,rows):
        #.............Calculate the Gini Impurity for a list of rows..............
        counts = class_counts(rows)
        impurity = 1
        for lbl in counts:
            prob_of_lbl = counts[lbl] / float(len(rows))
            impurity -= prob_of_lbl**2
        return impurity


    def info_gain(self,left, right, current_uncertainty):
    #.........Information Gain................
        p = float(len(left)) / (len(left) + len(right))
        return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

    # Calculate the uncertainy of our training data.
    current_uncertainty = gini(training_data)
    current_uncertainty

    # How much information do we gain by partioning on 'Green'?
    true_rows, false_rows = partition(training_data, Question(1, 1))
    info_gain(true_rows, false_rows, current_uncertainty)

    def find_best_split(self,rows):
        """Find the best question to ask by iterating over every feature / value
        and calculating the information gain."""
        best_gain = 0  # keep track of the best information gain
        best_question = None  # keep train of the feature / value that produced it
        current_uncertainty = gini(rows)
        n_features = len(rows[0]) - 1  # number of columns

        for col in range(n_features):  # for each feature

            values = set([row[col] for row in rows])  # unique values in the column

            for val in values:  # for each value

                question = Question(col, val)

                # try splitting the dataset
                true_rows, false_rows = partition(rows, question)

                # Skip this split if it doesn't divide the
                # dataset.
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                # Calculate the information gain from this split
                gain = info_gain(true_rows, false_rows, current_uncertainty)

                # You actually can use '>' instead of '>=' here
                # but I wanted the tree to look a certain way for our
                # toy dataset.
                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question


class Leaf:

    def __init__(self, rows):
        self.predictions = class_counts(rows)

#................Asks a question...................
class Decision_Node:
    #This holds a reference to the question, and to the two child nodes.


    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

class DecisionTree:
    def build_tree(self,rows):
    
        cal = Calculate()
        gain, question = cal.find_best_split(rows)
        if gain == 0:
            return Leaf(rows)

        true_rows, false_rows = partition(rows, question)

        true_branch = build_tree(true_rows)

        false_branch = build_tree(false_rows)

        return Decision_Node(question, true_branch, false_branch)

    #...............function to print tree.............
    def print_tree(self,node, spacing=""):
        

        if isinstance(node, Leaf):
            print (spacing + "Predict", node.predictions)
            return

        print (spacing + str(node.question))

        print (spacing + '--> True:')
        print_tree(node.true_branch, spacing + "  ")

        print (spacing + '--> False:')
        print_tree(node.false_branch, spacing + "  ")


    def classify(self,row, node):
        if isinstance(node, Leaf):
            return node.predictions
            
        if node.question.match(row):
            return classify(row, node.true_branch)
        else:
            return classify(row, node.false_branch)



    def print_leaf(self,counts):
        total = sum(counts.values()) * 1.0
        probs = {}
        for lbl in counts.keys():
            probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
        return probs


t=DecisionTree()   
my_tree = t.build_tree(training_data)

for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], t.print_leaf(t.classify(row, my_tree))))