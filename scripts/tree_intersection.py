class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    def inorder_traversal(node, values):
        if node is not None:
            inorder_traversal(node.left, values)
            values.add(node.value)
            inorder_traversal(node.right, values)

    values_tree1 = set()
    inorder_traversal(tree1, values_tree1)

    common_values = set()
    stack = [(tree2, common_values)]
    while stack:
        node, common_values = stack.pop()
        if node:
            if node.value in values_tree1:
                common_values.add(node.value)
            stack.append((node.left, common_values))
            stack.append((node.right, common_values))

    return common_values
