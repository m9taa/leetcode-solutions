# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Time:  O(n)
        # Space: O(1)
        if head is None or head.next is None:
            return head

        size = 1
        cur = head
        while cur.next is not None:
            size += 1
            cur = cur.next
        cur.next = head

        k = k % size

        tail = cur
        cur = head
        for _ in range(size - k):
            tail = cur
            cur = cur.next
        tail.next = None
        return cur
