# Given a classic linked list, reverse the list without using recursion
#
# First we'll need a Node in a classically linked list (a value and a next pointer)
# And then we'll need a place to store our linked nodes

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.root = None
    
    # Walk the list and add the node at the end
    def append_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    
    # This will allow us to visualize the entire linked list
    # Since we hace a singly linked list we need to walk the
    # entire list.
    def __str__(self):
        result = '{}'.format(str(self.root))
        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
            result = '{} -> {}'.format(result, str(current_node))
        
        return result
    
    # Reverse the list by swapping nodes through three variables
    # Flip the next reference to the previous as we go through the list
    def reverse(self):
        if self.root is None:
            return
        
        current_node = self.root
        next_node = None
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node 
            current_node = next_node
        
        self.root = previous_node

    