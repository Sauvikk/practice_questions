# Given a singly linked list, determine if its a palindrome.
# Return 1 or 0 denoting if its a palindrome or not, respectively.
#
# Notes:
# - Expected solution is linear in time and constant in space.
#
# For example,
#
# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  def reverse(self, head):
        current = head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

  def compare(self, first, second):
        while first and second:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return 0
        if first is None and second is None:
            return 1

  def solution(self, head):
        fast = head
        slow = head
        prevSlow = head
        while fast and fast.next:
            fast = fast.next.next
            prevSlow = slow
            slow = slow.next
        if fast:
            slow = slow.next
        second = slow
        prevSlow.next = None
        second = self.reverse(second)

        res = self.compare(head, second)

        if mid:
            prevSlow.next = mid
            mid.next = second
        else:
            prevSlow.next = second
        LinkedList.print_any(head)
        return res

A = LinkedList()
A.add(1)
res = Solution().solution(A.get_root())
print(res)
