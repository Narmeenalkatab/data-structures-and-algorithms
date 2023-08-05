import pytest
from scripts.tree_intersection import TreeNode, tree_intersection

def test_tree_intersection():
    # Test Case 1
    # Create tree1:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    # Create tree2:
    #     2
    #    / \
    #   4   6
    #  / \
    # 8   9
    tree2 = TreeNode(2)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(6)
    tree2.left.left = TreeNode(8)
    tree2.left.right = TreeNode(9)

    common_values = tree_intersection(tree1, tree2)
    assert common_values == {2, 4}

    # Test Case 2
    # Create tree3:
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(3)
    tree3.left.left = TreeNode(4)
    tree3.left.right = TreeNode(5)

    # Create tree4 (same as tree3):
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    tree4 = TreeNode(1)
    tree4.left = TreeNode(2)
    tree4.right = TreeNode(3)
    tree4.left.left = TreeNode(4)
    tree4.left.right = TreeNode(5)

    common_values = tree_intersection(tree3, tree4)
    assert common_values == {1, 2, 3, 4, 5}

    # Test Case 3
    # Create tree5:
    #     5
    #    / \
    #   3   8
    #  / \   \
    # 1   4   10
    tree5 = TreeNode(5)
    tree5.left = TreeNode(3)
    tree5.right = TreeNode(8)
    tree5.left.left = TreeNode(1)
    tree5.left.right = TreeNode(4)
    tree5.right.right = TreeNode(10)

    # Create tree6:
    #     3
    #    / \
    #   1   10
    #  / \   \
    # 4   5   12
    tree6 = TreeNode(3)
    tree6.left = TreeNode(1)
    tree6.right = TreeNode(10)
    tree6.left.left = TreeNode(4)
    tree6.left.right = TreeNode(5)
    tree6.right.right = TreeNode(12)

    common_values = tree_intersection(tree5, tree6)
    assert common_values == {3, 1, 4, 5, 10}

