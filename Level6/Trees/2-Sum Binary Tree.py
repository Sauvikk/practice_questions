# Given a binary search tree T, where each node contains a positive integer,
# and an integer K, you have to find whether or not there exist two different
# nodes A and B such that A.value + B.value = K.
#
# Return 1 to denote that two such nodes exist. Return 0, otherwise.
#
# Notes
# - Your solution should run in linear time and not take memory more than O(height of T).
# - Assume all values in BST are distinct.
#
# Example :
#
# Input 1:
#
# T :       10
#          / \
#         9   20
#
# K = 19
#
# Return: 1
#
# Input 2:
#
# T:        10
#          / \
#         9   20
#
# K = 40
#
# Return: 0


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:
    def __init__(self):
        self.stack_next = []
        self.stack_prev = []

    def assing(self, root):
        r1 = root
        r2 = root
        while r1:
            self.stack_next.append(r1)
            r1 = r1.left
        while r2:
            self.stack_prev.append(r2)
            r2 = r2.right

    def has_next(self):
        if len(self.stack_next) > 0:
            return True
        else:
            return False

    def has_prev(self):
        if len(self.stack_prev) > 0:
            return True
        else:
            return False

    def next(self):
        node = self.stack_next.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack_next.append(node)
                node = node.left
        return result

    def prev(self):
        node = self.stack_prev.pop()
        result = node.val
        if node.left:
            node = node.left
            while node:
                self.stack_prev.append(node)
                node = node.right
        return result

    def solution(self, root, target):
        self.assing(root)
        x1 = self.next()
        x2 = self.prev()
        while x1 < x2:
            if x1 + x2 == target:
                return 1
            if x1 + x2 < target:
                x1 = self.next()
            else:
                x2 = self.prev()
        return 0


node = Node(2)
node.left = Node(1)
node.right = Node(3)
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
res1 = Solution().solution(root, 4)
print(res1)
