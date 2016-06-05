# Find the lowest common ancestor in an unordered binary tree given two values in the tree.
#
#  Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or
#  directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
# Example :
#
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2_     0        8
#          /   \
#          7    4
# For the above tree, the LCA of nodes 5 and 1 is 3.
#
#  LCA = Lowest common ancestor
# Please note that LCA for nodes 5 and 4 is 5.
#
# You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
# No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
# There are no duplicate values.
# You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:
    def find_lca(self, root, node1, node2, is_present):
        if root is None:
            return None
        if root.val == node1:
            is_present[0] = True
            return root
        if root.val == node2:
            is_present[1] = True
            return root
        left_lca = self.find_lca(root.left, node1, node2, is_present)
        right_lca = self.find_lca(root.right, node1, node2, is_present)
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca

    def find(self, root, k):
        if root is None:
            return False
        if root.val == k or self.find(root.left, k) or self.find(root.right, k):
            return True
        return False

    def solution(self, root, node1, node2):
        is_present = [False, False]
        lca = self.find_lca(root, node1, node2, is_present)
        if (is_present[0] and is_present[1]) or (is_present[0] and self.find(lca, node2)) or (is_present[1]
                                                                                and self.find(lca, node1)):
            return lca
        return -1

node = Node(3)
node.left = Node(5)
node.right = Node(1)
node.left.left = Node(6)
node.left.right = Node(2)
node.left.right.left = Node(7)
node.left.right.right = Node(4)
node.right.left = Node(0)
node.right.right = Node(8)
res = Solution().solution(node, 5, 4)
print(res.val)

