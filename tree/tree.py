import csv
import time
import re

start_time = time.time()
attributes = ['url_length', 'Keywords', 'Url_count', 'spcl_char', 'Label']

class Train_Test_split:
    
    def __init__(self):
        self.training_data=[]
        self.testing_data=[]
        #split=0.2
        
    def train_test(self):
        data=[]
        with open("xssed.csv") as tsv:
            for line in csv.reader(tsv, delimiter=","):
                data.append(list(line))
        l=len(data)
        len_test=int(l*0.2)
        len_train=l-len_test
        for a in range (len_train):
            self.training_data.append(data[a])
        for b in range(len_train,l):
            self.testing_data.append(data[b])
        
        return self.training_data,self.testing_data

class Dataset:
    
    #......function returns unique value in the dataset......
    def unique_val(self,row,col):
        return set([r[col] for r in row])
    
    def count_label(self, rows):

        count = {}
        check=[]
        key=[]
        for row in rows:

            attribute =row[-1] #taking the label only
            if attribute not in count:
                count[attribute] = 0

            count[attribute] += 1

        #.....Checks if the label dictionary has more than 1 value......
        
        if len(count) ==1:
            return count
        else:
            if len(count) >1:
                check=list(count.values())
                key=list(count.keys())
                large=check[0]
                pos=0
                for i in range(len(check)):
                    if large < check[i]:
                        large = check[i]
                        pos=i
            new={str(key[pos]):large}
        return new

    
    def partition(self,rows,qtn):
        
        true_rows, false_rows = [], []
        for row in rows:
            if qtn.match(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

# ...................Class defines the questions in each node...........

class Question:
    
    def __init__(self, col, val):
        self.col = col
        self.val = val

    def match(self, row):
        values = row[self.col]
        return values >= self.val

    def __repr__(self):
        contn = '>='
        return "Is %s %s %s?" % (attributes[self.col], contn, str(self.val))

class Calculate:
    
    # .............Calculates Gini Impurity.................
    def gini(self, rows):
        d = Dataset()
        count = d.count_label(rows)
        impurity = 1
        for target in count:
            prob = count[target] / float(len(rows))
            impurity -= prob ** 2

        return impurity

   
    # ...........Calculates Information-gain............
    def info_gain(self, left_set, right_set, uncertainity):

        total_length = len(left_set) + len(right_set)
        prob = float(len(left_set)) / total_length
        gain = uncertainity - prob * \
               self.gini(left_set) - (1 - prob) * self.gini(right_set)

        return gain

    def find_best_split(self, rows):

        d = Dataset()
        best_gain = 0
        best_question = None  
        current_uncertainty = self.gini(rows)
        n_features = len(rows[0]) - 1  

        for col in range(n_features):  
            
            values = set([row[col] for row in rows])
            for val in values:  
                
                question = Question(col, val)
                true_rows, false_rows = d.partition(rows, question)
                if len(true_rows) == 0 or len(false_rows) == 0:
                    
                    continue
                # Calculates the information gain 
                gain = self.info_gain(
                    true_rows, false_rows, current_uncertainty)
                if gain >= best_gain:
                    
                    best_gain, best_question = gain, question

        return best_gain, best_question

class Leaf:
    
    def __init__(self, rows):
        d=Dataset()
        self.predictions = d.count_label(rows)

class Decision_Node:
    

    def __init__(self,question,true_branch,false_branch):
        
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

class Tree:
    
    def build_tree(self,rows):

        c= Calculate()
        d=Dataset()
        gain, question = c.find_best_split(rows)
        if gain == 0:
            return Leaf(rows)

        true_rows, false_rows = d.partition(rows, question)

        true_branch = self.build_tree(true_rows)

        false_branch = self.build_tree(false_rows)

        return Decision_Node(question, true_branch, false_branch)



def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""


    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    print (spacing + str(node.question))

    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


