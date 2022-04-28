import binary_tree

def test_binary_search_tree_insert():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)

    assert binary_search_tree.root.data == 5
    assert binary_search_tree.root.left.data == 3
    assert binary_search_tree.root.right.data == 8

def test_binary_search_tree_insert_duplicate():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    binary_search_tree.insert(5)
    binary_search_tree.insert(5)
    binary_search_tree.insert(8)

    assert binary_search_tree.root.data == 5
    assert binary_search_tree.root.left.data == 3
    assert binary_search_tree.root.right.data == 8

def test_binary_search_tree_find():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    root = binary_search_tree.root

    result1 = binary_search_tree.find(root, 5)
    result2 = binary_search_tree.find(root, 3)
    result3 = binary_search_tree.find(root, 8)
    result4 = binary_search_tree.find(root, 99)
    result5 = binary_search_tree.find(root, 1)
    
    assert result1.data == 5
    assert result2.data == 3
    assert result3.data == 8
    assert result4 is None
    assert result5 is None

def test_binary_search_tree_min():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    binary_search_tree.insert(4)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    root = binary_search_tree.root

    min = binary_search_tree.min(root)
    
    assert min.data == 1

def test_binary_search_tree_max():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(8)
    binary_search_tree.insert(9)
    binary_search_tree.insert(11)
    binary_search_tree.insert(10)
    binary_search_tree.insert(12)
    root = binary_search_tree.root

    max = binary_search_tree.max(root)
    
    assert max.data == 12

def test_binary_search_tree_delete_shift_right():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(8)
    root = binary_search_tree.root

    binary_search_tree.delete(root, 5)
    
    assert binary_search_tree.root.data == 8

def test_binary_search_tree_delete_shift_left():
    binary_search_tree = binary_tree.BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    root = binary_search_tree.root

    binary_search_tree.delete(root, 5)
    
    assert binary_search_tree.root.data == 3