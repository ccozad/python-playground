from logging import NullHandler


class BinaryTreeNode:
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

# We divide the tree using the rule that larger values go to the right
# and lesser values go to the left
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Preserve the structure of the binary search tree where larger values
    # are placed on the right and lesser values are placed on the left
    def insert(self, data):
        if self.root is None:
            self.root = BinaryTreeNode(data)
            return self.root
        else:
            inserted_node = BinaryTreeNode(data)
            parent_node = None
            current_node = self.root
            while current_node is not None:
                parent_node = current_node
                # No need to insert if the node is already in the tree
                if data == current_node.data:
                    return current_node
                elif data < current_node.data:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            
            inserted_node.parent = parent_node
            if data < parent_node.data:
                parent_node.left = inserted_node
            else:
                parent_node.right = inserted_node
            
            return inserted_node
    
    # Transfer old linkages to new linkages
    def shift(self, old_node: BinaryTreeNode, new_node: BinaryTreeNode):
        if old_node.parent is None:
            self.root = new_node
        elif old_node.data == old_node.parent.left.data:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        
        if new_node is not None:
            new_node.parent = old_node.parent

    # The simplest deletion happens when we are on a leaf node or alsmost at
    # at a leaf node. Things get more complicated when we delete an item from
    # the middle of the tree
    def delete(self, start_node: BinaryTreeNode, data):
        target_node = self.find(start_node, data)
        if target_node is None:
            return
        
        if target_node.left is None:
            self.shift(target_node, target_node.right)
        elif target_node.right is None:
            self.shift(target_node, target_node.left)
    
    # We can divide and conquer through the tree because of the
    # properties enforced by insert and delete.
    def find(self, start_node: BinaryTreeNode, data):
        current_node = start_node
        while current_node is not None and current_node.data != data:
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return current_node
    
    # Keep going right until we run out of nodes
    def max(self, start_node: BinaryTreeNode):
        current_node = start_node
        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node
    
    # Keep going left until we run out of nodes
    def min(self, start_node: BinaryTreeNode):
        current_node = start_node
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node
