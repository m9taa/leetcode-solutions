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
    bool isPalindrome(ListNode* head) {
        // Time:  O(n)
        // Space: O(1)
        ListNode *slow = head;
        ListNode *fast = head;
        ListNode *prev = nullptr;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        prev = slow;
        slow = slow->next;
        prev->next = nullptr;
        while (slow) {
            ListNode* tmp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = tmp;
        }
        fast = head;
        slow = prev;
        while (slow && fast) {
            if (slow->val != fast->val) {
                return false;
            }
            slow = slow->next;
            fast = fast->next;
        }
        return true;
    }
};
