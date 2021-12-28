#include <vector>
#include <queue>


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
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        // Time:  O(n * logk)
        // Space: O(k)
        ListNode* dummy = new ListNode(0);

        auto cmp = [](ListNode* lhs, ListNode* rhs) {return lhs->val > rhs->val; }; 
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> heap(cmp);

        for (const auto& head: lists) {
            if (head) {
                heap.emplace(head);
            }
        }
        ListNode* cur = dummy;
        while (!heap.empty()) {
            ListNode* node = heap.top();
            heap.pop();
            if (node->next) {
                heap.emplace(node->next);
            }
            cur->next = node;
            cur = cur->next;
        }

        return dummy->next;
    }
};
