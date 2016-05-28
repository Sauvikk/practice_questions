# Given a binary tree, return the inorder traversal of its nodes’ values.
#
# Example :
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Using recursion is not allowed.

from Level6.Trees.BinaryTree import BinaryTree


class Solution:

    def in_order(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
            else:
                result.append(top.val)
                stack.pop()
                if top.right:
                    stack.append(top.right)
        return result


A = BinaryTree()
A.insert(100)
A.insert(98)
A.insert(102)
A.insert(102)
A.insert(96)
A.insert(99)
A.insert(97)
A.insert(97)
res = Solution().in_order(A.root)
print(res)
