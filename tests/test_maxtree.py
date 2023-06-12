import pytest
from scripts.maxtree import BinaryTree, Node


def test_find_maximum_value():
    # Create a binary tree
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)

    # Find the maximum value in the tree
    max_value = tree.find_maximum_value()

    # Assert the result
    assert max_value == 11

# Another test case tree

def test_find_maximum_value2():
    tree =BinaryTree()
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(7)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(9)
    tree.root.left.right.right = Node(15)
    tree.root.right.right = Node(11)
    tree.root.right.right.left = Node(40)

    # Find the maximum value in the tree
    max_value = tree.find_maximum_value()

    # Assert the result
    assert max_value == 40