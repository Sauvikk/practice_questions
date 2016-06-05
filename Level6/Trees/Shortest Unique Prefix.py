# Find shortest unique prefix to represent each word in the list.
#
# Example:
#
# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
# NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.


class Node(object):
    def __init__(self):
        self.children = {}
        self.count = 0

    def insert(self, string, index):
        self.count += 1
        if index < len(string):
            current = string[index]
            if current not in self.children:
                self.children[current] = Node()
            child_node = self.children[current]
            child_node.insert(string, index+1)

    def search(self, string, index):
        if index > 0 and self.count == 1:
            prefix = string[0: index]
        else:
            ch = string[index]
            child_node = self.children[ch]
            prefix = child_node.search(string, index+1)
        return prefix


class Solution:

    def sol(self, strings):
        root = Node()
        for string in strings:
            root.insert(string, 0)
        prefixes = []
        for string in strings:
            shortest_unique_prefix = root.search(string, 0)
            prefixes.append(shortest_unique_prefix)
        return prefixes


res1 = Solution().sol(["geeksgeeks", "geeksquiz", "geeksforgeeks", "dove"])
print(res1)
