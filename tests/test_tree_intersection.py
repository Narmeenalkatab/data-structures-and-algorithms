import pytest
from scripts.tree_intersection  import TreeNode, tree_intersection

def test_tree_intersection():
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
