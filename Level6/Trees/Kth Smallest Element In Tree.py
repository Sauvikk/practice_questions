# Given a binary search tree, write a function to find the kth smallest element in the tree.
#
# Example :
#
# Input :
#   2
#  / \
# 1   3
#
# and k = 2
#
# Return : 2
#
# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def in_order(self, root, k):
        if not root:
            return root
        stack = [root]
        while stack:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
            else:
                result = stack.pop()
                k -= 1
                if k == 0:
                    return result.val
                if top.right:
                    stack.append(top.right)


node = Node(2)
node.left = Node(1)
node.right = Node(3)
res = Solution().in_order(node, 2)
print(res)
