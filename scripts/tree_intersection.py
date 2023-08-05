class Hashmap:
    def __init__(self):
        self._data = {}

    def add(self, key, value):
        self._data[key] = value

    def contains(self, key):
        return key in self._data

    def get(self, key):
        return self._data.get(key)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    def inorder_traversal(node, hashmap):
        if node is not None:
            inorder_traversal(node.left, hashmap)
            hashmap.add(node.value, True)
            inorder_traversal(node.right, hashmap)

    common_values = set()
    hashmap = Hashmap()
    inorder_traversal(tree1, hashmap)

    stack = [tree2]
    while stack:
        node = stack.pop()
        if node:
            if hashmap.contains(node.value):
                common_values.add(node.value)
            stack.append(node.left)
            stack.append(node.right)

    return common_values
