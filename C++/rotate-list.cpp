// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // Time:  O(n)
        // Space: O(1)
        if (head == nullptr || head->next == nullptr ) {
            return head;
        }

        int size = 1;
        ListNode* cur = head;
        while (cur->next) {
            size++;
            cur = cur->next;
        }
        cur->next = head;

        k %= size;

        ListNode* tail = cur;
        cur = head;
        for (int i = 0; i < size - k; cur = cur->next, i++) {
            tail = cur;
        }
        tail->next = nullptr;
        return cur;
    }
};
