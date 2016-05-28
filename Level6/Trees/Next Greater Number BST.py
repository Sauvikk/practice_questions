# Given a BST node, return the node which has value just greater than the given node.
#
# Example:
#
# Given the tree
#
#                100
#               /   \
#             98    102
#            /  \
#          96    99
#           \
#            97
# Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
# If there are no successor in the tree ( the value is the largest in the tree, return NULL).
#
# Using recursion is not allowed.
#
# Assume that the value is always present in the tree.


from Level6.Trees.BinaryTree import BinaryTree


class Solution:
    def find(self, root, data):
        while root:
            if root.val == data:
                return root
            if data < root.val:
                root = root.left
            else:
                root = root.right

    def find_min(self, root):
        if root is None:
            return root
        while root.left:
            root = root.left
        return root

    def solution(self, root, data):
        current = self.find(root, data)
        if current is None:
            return None
        if current.right:
            return self.find_min(current.right)
        else:
            successor = None
            ancestor = root
            while ancestor:
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
        return successor


A = BinaryTree()
A.insert(100)
A.insert(98)
A.insert(102)
A.insert(102)
A.insert(96)
A.insert(99)
A.insert(97)
A.insert(97)
res = Solution().solution(A.root, 97)
print(res)
