import binary_tree

class BinarySearchTreeWalker:
    # Traverse the current node's left subtree and store what we find along the way
    # Visit the current node
    # Traverse the current node's right subtree.
    def inorder(self, binary_search_tree: binary_tree.BinarySearchTree):
        results = []
        node_stack = []
        current_node = binary_search_tree.root
        while current_node is not None or len(node_stack) > 0:
            while current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left
            
            if current_node is None and len(node_stack) > 0:
                node = node_stack[-1]
                node_stack.pop()
                results.append(node.data)
                current_node = node.right

        return results

    # Traverse the current node's right subtree and store what we find along the way
    # Visit the current node
    # Traverse the current node's left subtree.
    def reverse_inorder(self, binary_search_tree: binary_tree.BinarySearchTree):
        results = []
        node_stack = []
        current_node = binary_search_tree.root
        while current_node is not None or len(node_stack) > 0:
            while current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.right
            
            if current_node is None and len(node_stack) > 0:
                node = node_stack[-1]
                node_stack.pop()
                results.append(node.data)
                current_node = node.left

        return results

