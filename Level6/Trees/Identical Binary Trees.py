# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#
#    1       1
#   / \     / \
#  2   3   2   3
#
# Output :
#   1 or True


from Level6.Trees.BinaryTree import BinaryTree


class Solution:

    def solution(self, rootA, rootB):

        if rootA == rootB:
            print('h')
            return True

        if rootA is None or rootB is None:
            return False

        # if rootA is None and rootB is None:
        #     return True

        return ((rootA.val == rootB.val) and self.solution(rootA.left, rootB.left) and
                    self.solution(rootA.right, rootB.right))


A = BinaryTree()
A.insert(100)
A.insert(102)
A.insert(96)
B = BinaryTree()
B.insert(100)
B.insert(102)
B.insert(96)
res = Solution().solution(A.root, B.root)
print(res)
