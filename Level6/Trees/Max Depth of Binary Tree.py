# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the nearest leaf node.
#
#  NOTE : The path has to end on a leaf node.
# Example :
#
#          1
#         /
#        2
# max depth = 2.


from Level6.Trees.BinaryTree import BinaryTree


class Solution:

    def solution(self, root):
        if root is None:
            return 0
        left_depth = self.solution(root.left)
        right_depth = self.solution(root.right)
        return left_depth+1 if left_depth > right_depth else right_depth+1


A = BinaryTree()
A.insert(10)
A.insert(8)
A.insert(2)
A.insert(3)
A.insert(5)
A.insert(2)
res = Solution().solution(A.root)
print(res)
