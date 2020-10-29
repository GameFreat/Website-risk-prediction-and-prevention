import numpy as np
from collections import Counter

#........calculates Entropy..........
def Entropy(attribute):

    frequency = np.bincount(attribute) #collects the number of occurances
    prob = frequency/len(attribute) #length of attributs no of total samples 
    for p in prob :
        if p > 0:
            return -np.sum([p * np.log2(p)]) #returns the entropy

#.........contains info of our node........
class Node:

    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def Checkif_leaf(self):
        return self.value is not None #if at leaf node returns the label if 1 or 0


class DecisionTree:

    def __init__(self, min_split=2, max_depth=100, feature_number=None):
    
        #......assigning default values......
        self.min_split = min_split
        self.max_depth = max_depth
        self.feature_number = feature_number
        self.root = None

    def fit(self,x_data,y_data):
        
        x_data = np.array(x_data)
        self.feature_number = x_data.shape[1] if not self.feature_number else min(self.feature_number, x_data.shape[1])
        self.root = self.Build_tree(x_data,y_data)
    
    def predict(self ,x_data):
        
        #......Tree traversal to predict.......

        for x in x_data:
            return np.array([self.Tree_traverse(x, self.root)])

     #..........Calculates Information gain...........
    def Information_gain(self, y, X_column, split_thresh):
        
        #..........Calculates Entropy of Parent Node..........
        parent_entropy = Entropy(y)


        left_child, right_child = self.Split(X_column, split_thresh)

        if len(left_child) == 0 or len(right_child) == 0:
            return 0
       
        count = len(y)

        count_left= len(left_child)
        count_right=len(right_child)
        ent_left= Entropy(y[left_child])
        ent_right=Entropy(y[right_child])
        child_entropy = (count_left / count) * ent_left + (count_right / count) * ent_right

        # information gain is difference in loss before vs. after split
        gain = parent_entropy - child_entropy
        return gain

    def Build_tree(self, x, y, depth=0):
        
        print(x.shape)
        samples = x.shape[1]
        features = x.shape[2]
        count = np.unique(y)
        labels = len(count)
        
        #stopping criteria
          #1.max depth
          #2.min samples at nodes
          #3.no more class

        if(depth >= self.max_depth or labels == 1 or samples < self.min_split):
            
            leaf_type = self.Most_common(y)
            return Node(value=leaf_type)

        feature_index = np.random.choice(features,self.feature_number,replace = False)  
        
        #.....Greedy Search.....
        best_feature,best_thresh = self.best_Criteria(x,y,feature_index)
        
        # .......grow the children that result from the split ......
        
        left_index, right_index = self.Split(x[:, best_feature], best_thresh)

        left = self.Build_tree(x[left_index, :], y[left_index], depth+1)
        right = self.Build_tree(x[right_index, :], y[right_index], depth+1)
        return Node(best_feature, best_thresh, left, right)

    def best_Criteria(self, x, y, feature):
        
        best_gain = -1
        best_feature = None
        best_threshold=None

        for index in feature:
            X_column = x[:, index]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self.Information_gain(y, X_column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = index
                    best_threshold = threshold

        return best_feature,best_threshold

    def Split(self, X_column, split_thresh):
    
        left_index = np.argwhere(X_column <= split_thresh).flatten()
        right_index = np.argwhere(X_column > split_thresh).flatten()
        return left_index, right_index

    def Traverse_tree(self, x, node):
        if node.Checkif_leaf():
            return node.value

        if x[node.feature] <= node.threshold:
            return self.Traverse_tree(x, node.left)
        return self.Traverse_tree(x, node.right)


    def Most_common(self,y):
        
        count = Counter(y)
        #returns a list of tuples so to get the value only
        #most_commom_label = count.most_common(1)[0][0] 
        return count.most_common(1)[0][0] 
