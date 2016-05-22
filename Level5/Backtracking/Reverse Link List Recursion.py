# Reverse Link List Recursion
# Reverse a linked list using recursion.
#
# Example :
# Given 1->2->3->4->5->NULL,
#
# return 5->4->3->2->1->NULL.

import sys
sys.setrecursionlimit(100)
from Level4.LinkedLists.LinkedList import LinkedList, Node


def solution(currentNode):
        if not currentNode:
            return None
        if currentNode.next is None:
            return currentNode
        rest = solution(currentNode.next)
        currentNode.next.next = currentNode
        currentNode.next = None
        return rest


A = LinkedList()
A.add(9)
A.add(8)
A.add(8)
A.add(8)
A.print()
res1 = solution(A.get_root())
LinkedList.print_any(res1)
