class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def find_maximum_value(self):
        """
        Find the maximum value in the binary tree.

        Returns:
            The maximum value in the binary tree.
        """
        if self.root is None:
            return None

        def dfs(node, max_value):
            """
            Helper function to perform depth-first search and find the maximum value.

            Args:
                node: The current node being visited.
                max_value: The maximum value encountered so far.

            Returns:
                The maximum value encountered in the subtree rooted at the current node.
            """
            if node is None:
                return max_value

            if node.value > max_value:
                max_value = node.value

            max_value = dfs(node.left, max_value)
            max_value = dfs(node.right, max_value)

            return max_value

        return dfs(self.root, float('-inf'))
