# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(head):
        if head is None or head.next is None:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

A = LinkedList()
A.add(1)
A.add(1)
A.add(1)
A.add(1)
A.add(1)
A.add(2)
A.add(2)
A.add(2)
A.add(3)
A.add(3)
A.add(3)
A.add(3)
A.add(3)
A.add(3)
A.add(3)
A.add(4)
A.add(5)
A.print()
res = Solution.solution(A.get_root())
LinkedList.print_any(res)



# def solution(head):
#         if head is None or head.next is None:
#             return head
#         prev = head
#         curr = head.next
#         while curr:
#             if prev.val == curr.val:
#                 prev.next = curr.next
#                 curr = curr.next
#             else:
#                 prev = curr
#                 curr = curr.next
#         return head
