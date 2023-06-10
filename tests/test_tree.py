
from scripts.trees import BinarySearchTree,BinaryTree,Node

# Test Cases
def test_binary_tree():
    # Test empty tree
    binary_tree = BinaryTree()
    assert binary_tree.pre_order() == []
    assert binary_tree.in_order() == []
    assert binary_tree.post_order() == []

    # Test tree with a single root node
    binary_tree.root = Node(1)
    assert binary_tree.pre_order() == [1]
    assert binary_tree.in_order() == [1]
    assert binary_tree.post_order() == [1]


def test_binary_search_tree():
    # Test adding left and right children to a node
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(2)
    binary_search_tree.add(1)
    binary_search_tree.add(3)
    assert binary_search_tree.pre_order() == [2, 1, 3]
    assert binary_search_tree.in_order() == [1, 2, 3]
    assert binary_search_tree.post_order() == [1, 3, 2]

    # Test contains method
    assert binary_search_tree.contains(2) is True
    assert binary_search_tree.contains(1) is True
    assert binary_search_tree.contains(3) is True
    assert binary_search_tree.contains(4) is False


# Run 
test_binary_tree()
test_binary_search_tree()
