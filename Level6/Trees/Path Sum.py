# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
# values along the path equals the given sum.
#
# Example :
#
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def solution(self, root, target):
        if root is None:
            return False
        if root.val == target and root.left is None and root.right is None:
            return True
        return self.solution(root.left, target-root.val) or self.solution(root.right, target-root.val)

A = BinaryTree()
A.insert(10)
A.insert(8)
A.insert(2)
A.insert(3)
A.insert(5)
A.insert(2)
res = Solution().solution(A.root, 14)
print(res)
