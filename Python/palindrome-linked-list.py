# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Time:  O(n)
        # Space: O(1)
        slow, fast, prev = head, head, None
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        prev = slow
        slow = slow.next
        prev.next = None
        while (slow):
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        fast = head
        slow = prev
        while(slow and fast):
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
