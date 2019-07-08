
"""Linked lits
"""


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.current_node = None

    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.current_node
        self.current_node = new_node

    def list_print(self):
        node = self.current_node
        while node:
            print(node.data)
            node = node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node('da')

    ll.list_print()
