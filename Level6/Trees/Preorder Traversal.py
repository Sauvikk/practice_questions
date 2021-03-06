# Given a binary tree, return the postorder traversal of its nodes’ values.
#
# Example :
#
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
#
# Using recursion is not allowed.


from Level6.Trees.BinaryTree import BinaryTree


class Solution:
    def pre_order(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            top = stack.pop()
            result.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
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
res = Solution().pre_order(A.root)
print(res)
