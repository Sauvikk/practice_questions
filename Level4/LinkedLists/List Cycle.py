# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Try solving it using constant additional space.
#
# Example :
#
# Input :
#
#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4
#
# Return the node corresponding to node 3.
# http://javabypatel.blogspot.in/2015/12/detect-loop-in-linked-list.html


from Level4.LinkedLists.LinkedList import LinkedList


class Solution:

  @staticmethod
  def solution(head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

A = LinkedList()
A.add(9)
A.add(8)
A.add(7)
A.add(6)
A.add(5)
A.add(4)
A.add(3)
A.add(2)
A.add(1)
A.add(0)
A.get_root().next.next.next.next.next.next.next.next.next.next = A.get_root().next.next.next.next
res = Solution.solution(A.get_root())
print(res.val)
