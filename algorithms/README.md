# Introduction

The section explores various algorithms. Many of these classic algorithms exist in various standard libraries and popular third party libraries. The reader is encouraged to understand these data structures in terms of the style of problem solving and thinking involved. Ideas explored in data structures may lend to original solutions for niche applications.

# Execution

All algorithms are exercised by way of unit tests using PyTest. Running PyTest from the directory will run all algorithm tests. These tests serve as documentation on usage if you would like to use an algorithm in your projects.

# Algorithms

## [Binary Search](/algorithms/binary_search_client.py)

Binary search is a divide and conquer search algorithm that splits the search space in half with each pass. It has a worst case performance of O(log n). Binary Search relies on the data being pre-sorted to take advantage of the ording to decide which half of the search space to eliminate. See the Wikipedia article on binary search for more details: https://en.wikipedia.org/wiki/Binary_search_algorithm 

## [Binary Search Tree](/algorithms/binary_tree.py)

A Binary Tree is a tree data structure where each node can have one parent and no more than two children, called the parent, left and right respectively. We can take this data structure and add a constraint that for a given node, all nodes to the left are less than the node and all nodes to the right are greater than the node. This bifurcation allows divide and conquer techniques to be used. Search performance depends on the height of the tree and is expressed as O(h) where h is the height of the tree. "unbalanced" trees where the height may approach n, the number of nodes, in which case search performance is similar to a linked list. See the Wikipedia article on Binary Search Trees for more details: https://en.wikipedia.org/wiki/Binary_search_tree

## [Hamming distance](/algorithms/hamming_distance.py) 

Number of positions in which symbols differ for two equal length strings. Read more at https://en.wikipedia.org/wiki/Hamming_distance 

## [Inorder Tree Traversal](/algorithms/binary_search_tree_walker.py) 

The nodes of a binary tree can be visited in a variety of ways. The inorder traversal uses a stack to sequence nodes correctly and results in the nodes being visited in ascending order.

## [Merge Sort](/algorithms/merge_sort_client.py)

Merge sort is a divide and conquer sorting algorithm that sorts small lists and merges the smaller lists into larger lists with the correct ordering. Merge sort has a worse case performace of O(n log n). See the Wikipedia article on merge sort for more details: https://en.wikipedia.org/wiki/Merge_sort 

## [Reverse Inorder Tree Traversal](/algorithms/binary_search_tree_walker.py) 

The nodes of a binary tree can be visited in a variety of ways. The reverse inorder traversal uses a stack to sequence nodes correctly and results in the nodes being visited in descending order.

**[Back to start](https://github.com/ccozad/python-playground)**