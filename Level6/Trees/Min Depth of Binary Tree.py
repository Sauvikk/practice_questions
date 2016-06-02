# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
#  NOTE : The path has to end on a leaf node.
# Example :
#
#          1
#         /
#        2
# min depth = 2.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def solution(self, root):
        if root is None:
            return 0
        left_depth = self.solution(root.left)
        right_depth = self.solution(root.right)
        return left_depth+1 if left_depth < right_depth else right_depth+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = Solution().solution(root)
print(res)



