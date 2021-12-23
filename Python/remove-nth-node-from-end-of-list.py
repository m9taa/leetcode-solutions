# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Time:  O(n)
        # Space: O(1)
        slow, fast = head, head

        while n > 0:
            fast = fast.next
            n -= 1

        if fast is None:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
