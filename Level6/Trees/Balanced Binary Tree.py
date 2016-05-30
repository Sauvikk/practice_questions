# Given a binary tree, determine if it is height-balanced.
#
# Height-balanced binary tree : is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#           1
#          / \
#         2   3
#
# Return : True or 1
#
# Input 2 :
#          3
#         /
#        2
#       /
#      1
#
# Return : False or 0
#          Because for the root node, left subtree has depth 2 and right subtree has depth 0.
#          Difference = 2 > 1.


from Level6.Trees.BinaryTree import BinaryTree


class Solution:

    def is_balanced(self, root):
        if root is None:
            return True
        if self.get_depth(root) == -1:
            return False
        return True

    def get_depth(self, root):
        if root is None:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1


A = BinaryTree()
A.insert(100)
A.insert(102)
A.insert(96)
res = Solution().is_balanced(A.root)
print(res)
