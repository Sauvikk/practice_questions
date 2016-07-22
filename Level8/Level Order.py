# Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Also think about a version of the question where you are asked to do a
# level order traversal of the tree when depth of the tree is much greater than number of nodes on a level.

from Level6.Trees.BinaryTree import BinaryTree, Node
from collections import deque

class Solution:
    def sol(self, root):
        result = []
        node_value = []
        if root is None:
            return result
        current = deque()
        next = deque()
        current.append(root)
        while len(current) != 0:
            node = current.popleft()
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            node_value.append(node.val)
            if len(current) == 0:
                current = next
                next = deque()
                result.append(node_value[0:])
                node_value.clear()
        return result


r = Node(3)
r.left = Node(9)
r.right = Node(20)
r.right.left = Node(15)
r.right.right = Node(7)
print(Solution().sol(r))

