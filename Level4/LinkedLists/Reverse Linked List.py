# Reverse a linked list. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL,
#
# return 5->4->3->2->1->NULL.

from Level4.LinkedLists.LinkedList import LinkedList


class Solution:

  @staticmethod
  def solution(head):
        current = head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

A = LinkedList()
A.add(0)
A.add(10)
A.add(20)
A.add(30)
A.add(40)
A.add(50)
A.add(60)
A.add(70)
res = Solution.solution(A.get_root())
while res:
    print(res.val)
    res = res.next
