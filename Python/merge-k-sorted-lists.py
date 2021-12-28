import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        h = []
        for i, first_node in enumerate(lists):
            if first_node:
                heapq.heappush(h, (first_node.val, i))

        head = cur = None
        if h:
            value, list_idx = heapq.heappop(h)
            head = cur = lists[list_idx]
            if cur.next:
                heapq.heappush(h, (cur.next.val, list_idx))
                lists[list_idx] = cur.next
        while h:
            value, list_idx = heapq.heappop(h)
            node = lists[list_idx]
            if node.next:
                heapq.heappush(h, (node.next.val, list_idx))
                lists[list_idx] = node.next
            cur.next = node
            cur = node

        return head
