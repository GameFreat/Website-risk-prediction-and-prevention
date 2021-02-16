from decision_tree import *
import treelib
sample=[
[60,2,0,8,1],
[11,0,0,2,0],
[632,12,0,14,1],
[20,1,0,2,0]]

#...........Testing done right(PASSED)..............
#..........testing decision_tree.py class.........

def test_get_unique_val():
    d=Data()
    val=d.get_unique_val(sample,0)
    print(val)
    assert val=={60,11,632,20}

def test_count_Class():
    d=Data()
    val=d.count_Class(sample)
    assert val =={1:2,0:2}

def test_Qtn():
    q=Node_Rules(1,3)
    val=q
    assert str(val) == 'Is Keywords >= 3?'

def test_partition():
    d=Data()
    q=Node_Rules(3,3)
    t,f=d.partition(sample,q)
    assert t == [[60,2,0,8,1],[632,12,0,14,1]]
    assert f ==[[11,0,0,2,0],[20,1,0,2,0]]

def test_gini():
    no_mixing=[[0],[0]]
    c=Calculate()
    val = c.gini_idx(no_mixing)
    assert val == 0.0


def test_gini():
    with_mixing=[[0],[1]]
    c=Calculate()
    val = c.gini_idx(with_mixing)
    assert val == 0.5

def test_gain():
    c=Calculate()
    d=Data()
    uncertainity = c.gini_idx(sample)
    q=Node_Rules(3,3)
    t,f=d.partition(sample,q)
    val = c.information_gain(t,f,uncertainity)
    assert val== 0.5

def test_best_split():
    c=Calculate()
    gain,qtn=c.find_best_split(sample)
    assert str(qtn) == 'Is spcl_char >= 8?' 

def test_tree():
    t=treelib.Tree()
    b=DecisionTree()
    const_tree=treelib.Tree()
    t.create_node('Is spcl_char >= 8?','Is spcl_char >= 8?')
    my_tree = b.build_tree(sample, const_tree, '')
    assert t.show()== const_tree.show()
