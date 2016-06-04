# Given a binary tree, invert the binary tree and return it.
# Look at the example for more details.
#
# Example :
# Given binary tree
#
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# invert and return
#
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def solution(self, root):
        if not root:
            return root
        root.left = self.solution(root.left)
        root.right = self.solution(root.right)
        root.left, root.right = root.right, root.left
        return root

node = Node(1)
node.left = Node(2)
node.right = Node(3)
BinaryTree().in_order(node)
res1 = Solution().solution(node)
print('-------')
BinaryTree().in_order(res1)
