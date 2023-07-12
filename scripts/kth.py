class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node =Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def kth_from_end(self, k):
        if k < 0 or self.head is None:
            return None
        slow = fast = self.head
        for _ in range(k):
           if fast is None:
             return None
           fast = fast.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow.value if slow is not None else None


       #Stretch Goal
    def find_middle(self):
        if self.head is None:
            return None

        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.value
