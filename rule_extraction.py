#........................Krishnapriya............................
class Rule_extractor:
 
    def Leaf_count(self):
        t = DecisionTree()
        leaf = []
        unique =[]
        count_leaf =0
        for i in range(len(training_data)):
            leaf.append(t.classify(training_data[i], my_tree))


        for x in leaf: 
                # check for unique leaf values
                if x not in unique: 
                    unique.append(x) 

        return len(unique),unique

    #def values (self,rule):
        #return my_tree.rule
    #........Need a tree Trversal function............
    def Tree_traversal(self,leaf):
        rules=[]


        if isinstance(node, Leaf):
            #print (spacing + "Node", node.predictions)
            return

        rules.append(str(node.rule))

        #print (spacing + '--> Yes:')
        self.print_tree(node.right_node, spacing + "\t")

        #print (spacing + '--> No:')
        self.print_tree(node.left_node, spacing + "\t")
        print(rules)

    def extractor(self):
        rules ={}
        leaf_count,leaf_val = self.Leaf_count()
        side = ['right_node','left_node']
        self.Tree_traversal(training_data)
        for count in range (leaf_count):
            rules[count+1]=0#self.Tree_traversal(leaf) #self.values(count)

r = Rule_extractor()
r.extractor()