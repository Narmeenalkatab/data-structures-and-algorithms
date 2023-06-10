class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        #root-left-right
        return self._pre_order_recursive(self.root, [])

    def _pre_order_recursive(self, node, traversal):
        if node:
            traversal.append(node.value)
            traversal = self._pre_order_recursive(node.left, traversal)
            traversal = self._pre_order_recursive(node.right, traversal)
        return traversal

    def in_order(self):
        #left-root-right
        return self._in_order_recursive(self.root, [])

    def _in_order_recursive(self, node, traversal):
        if node:
            traversal = self._in_order_recursive(node.left, traversal)
            traversal.append(node.value)
            traversal = self._in_order_recursive(node.right, traversal)
        return traversal

    def post_order(self):
        #left-right-root
        return self._post_order_recursive(self.root, [])

    def _post_order_recursive(self, node, traversal):
        if node:
            traversal = self._post_order_recursive(node.left, traversal)
            traversal = self._post_order_recursive(node.right, traversal)
            traversal.append(node.value)
        return traversal


class BinarySearchTree(BinaryTree):
    def add(self, value):
        self.root = self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._add_recursive(node.left, value)
        else:
            node.right = self._add_recursive(node.right, value)
        return node

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)
