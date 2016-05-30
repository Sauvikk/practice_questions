# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# Example :
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric.
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


from Level6.Trees.BinaryTree import BinaryTree


class Solution:
    def is_symmetric(self, root_left, root_right):
        if root_left is None and root_right is None:
            return True
        elif root_left is None or root_right is None:
            return False

        if root_right.val != root_left.val:
            return False

        if not self.is_symmetric(root_left.left, root_right.right):
            return False
        if not self.is_symmetric(root_left.right, root_right.left):
            return False
        return True

    def solution(self, root):
        if root is None:
            return True
        return self.is_symmetric(root.left, root.right)


A = BinaryTree()
A.insert(1)
A.insert(2)
A.insert(2)
A.insert(3)
A.insert(4)
A.insert(3)
A.insert(4)
res = Solution().solution(A.root)
print(res)
