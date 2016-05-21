# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
#  only nodes itself can be changed.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr = dummy_head
        while curr.next and curr.next.next:
            n1 = curr.next
            n2 = curr.next.next
            n1.next = n2.next
            n2.next = n1
            curr.next = n2
            curr = n1
        return dummy_head.next

A = LinkedList()
A.add(0)
A.add(2)
A.print()
res = Solution.solution(A.get_root())
LinkedList.print_any(res)
