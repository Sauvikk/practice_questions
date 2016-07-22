# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# Example :
#
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def sum_max(self, root, result):
        if root is None:
            return 0
        left = self.sum_max(root.left, result)
        right = self.sum_max(root.right, result)
        curr = max(root.val, max(root.val+left, root.val+right))
        result[0] = max(result[0], max(curr, root.val+left+right))
        return curr

    def sol(self, root):
        result = [-2**31]
        self.sum_max(root, result)
        return result[0]


r = Node(1)
r.left = Node(2)
r.right = Node(3)
print(Solution().sol(r))
