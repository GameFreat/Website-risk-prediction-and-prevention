from tree import *
import time
import pickle as c

class Test:    
    def __init__(self):
        self.count =0
        
    def classify(self,row, node):
        if isinstance(node, Leaf):
            return node.predictions

        if node.question.match(row):
            return self.classify(row, node.true_branch)
        else:
            return self.classify(row, node.false_branch)
        
    def print_leaf(self,counts):
        total = sum(counts.values()) * 1.0
        probs = {}
        for lbl in counts.keys():
            probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
        return probs
    
    def accuracy(self):
        c=0
        for row in testing_data:
           
            lab=self.classify(row,my_tree)
            l = str(row[-1])
            if l in lab:
                c += 1
        #print(c)
    
        acc = c/len(testing_data)
        print('Accuracy of the model ::',acc)

    def save(self,clf, name):
        with open(name, 'wb') as fp:
            c.dump(clf, fp)
        print ("Model saved")

tts=Train_Test_split()
training_data,testing_data= tts.train_test()

t=Tree()
my_tree = t.build_tree(training_data)

print_tree(my_tree)   

t=Test()
t.accuracy()
t.save(my_tree, "text-classifier.mdl")     #storing trained file

end_time = time.time()
print('Time taken is::',end_time-start_time)

