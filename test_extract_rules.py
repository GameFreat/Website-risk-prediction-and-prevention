from decision_tree import *
from extract_rules import *
sample=[
[60,2,0,8,1],
[11,0,0,2,0],
[632,12,0,14,1],
[20,1,0,2,0]]

def test_rules():
    b=DecisionTree()
    const_tree=treelib.Tree()
    my_tree = b.build_tree(sample, const_tree, '')
    e=ExtractRules()
    e.dfs([],const_tree,const_tree.root)
    val=e.create_rules(const_tree,const_tree.root)

    print(val)
    assert val==[['Is spcl_char >= 8?', '{1: 2}'],['Is spcl_char < 8?', '{0: 2}']]
    