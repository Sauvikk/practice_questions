# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
#
# For example, given following linked lists :
#
#   5 -> 8 -> 20
#   4 -> 11 -> 15
# The merged list should be :
#
# 4 -> 5 -> 8 -> 11 -> 15 -> 20


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.val < node2.val:
            result = node1
            result.next = Solution.solution(node1.next, node2)
        else:
            result = node2
            result.next = Solution.solution(node1, node2.next)
        return result

A = LinkedList()
A.add(20)
A.add(8)
A.add(5)
B = LinkedList()
B.add(15)
B.add(11)
B.add(4)
res = Solution.solution(A.get_root(), B.get_root())
LinkedList.print_any(res)

# iterative solution
# @staticmethod
#   def solution(node1, node2):
#         result = Node(0)
#         current = result
#         while True:
#             if not node1:
#                 current.next = node2
#                 break
#             if not node2:
#                 current.next = node1
#                 break
#             if node1.val < node2.val:
#                 current.next = node1
#                 node1 = node1.next
#             else:
#                 current.next = node2
#                 node2 = node2.next
#             current = current.next
#         return result.next
