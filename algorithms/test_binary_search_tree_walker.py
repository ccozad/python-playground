import binary_tree
import binary_search_tree_walker

def test_inorder():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    binary_search_tree.insert(4)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    
    bstw = binary_search_tree_walker.BinarySearchTreeWalker()
    results = bstw.inorder(binary_search_tree)
    
    assert len(results) == 6
    assert results[0] == 1
    assert results[1] == 2
    assert results[2] == 3
    assert results[3] == 4
    assert results[4] == 5
    assert results[5] == 8

def test_reverse_inorder():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    binary_search_tree.insert(4)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    
    bstw = binary_search_tree_walker.BinarySearchTreeWalker()
    results = bstw.reverse_inorder(binary_search_tree)
    
    assert len(results) == 6
    assert results[0] == 8
    assert results[1] == 5
    assert results[2] == 4
    assert results[3] == 3
    assert results[4] == 2
    assert results[5] == 1