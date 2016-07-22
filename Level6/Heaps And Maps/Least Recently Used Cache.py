# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRUCache will be initialized with an integer corresponding to its capacity.
# Capacity indicates the maximum number of unique keys it can hold at a time.
#
# Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item.
# “Least recently used” item is the one with the oldest access time.
#
#  NOTE: If you are using any global variables, make sure to clear them in the constructor.
# Example :
#
# Input :
#          capacity = 2
#          set(1, 10)
#          set(5, 12)
#          get(5)        returns 12
#          get(1)        returns 10
#          get(10)       returns -1
#          set(6, 14)    this pushes out key = 5 as LRU is full.
#          get(5)        returns -1


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.end = None
        self.map_p = {}

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev

    def set_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.end is None:
            self.end = self.head

    def get(self, key):
        if key in self.map_p:
            node = self.map_p[key]
            self.remove(node)
            self.set_head(node)
            return node.val
        return -1

    def set(self, key, value):
        if key in self.map_p:
            node = self.map_p[key]
            node.val = value
            self.remove(node)
            self.set_head(node)
        else:
            node = Node(key, value)
            if len(self.map_p) >= self.capacity:
                self.map_p.pop(self.end.key)
                self.remove(self.end)
                self.set_head(node)
            else:
                self.set_head(node)
            self.map_p[key] = node

lru = LRUCache(2)
lru.set(1, 10)
lru.set(5, 12)
print(lru.get(5))
print(lru.get(1))
print(lru.get(10))
lru.set(6, 14)
print(lru.get(5))




