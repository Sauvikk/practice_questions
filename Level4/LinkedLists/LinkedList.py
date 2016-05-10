# Implementation of link list in python


class Node(object):

    def __init__(self, d, n=None):
        self.val = d
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.val

    def set_data(self, d):
        self.val = d


class LinkedList (object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_root(self):
        return self.root

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    @staticmethod
    def print_any(node):
        current = node
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def print(self):
        current = self.get_root()
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

