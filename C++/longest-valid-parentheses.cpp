#include <algorithm>
#include <stack>
#include <string>


class Solution {
public:
    int longestValidParentheses(std::string s) {
        // Time:  O(n)
        // Space: O(n)
        int maxLength = 0;
        std::stack<int> stk;
        stk.push(-1);

        for (size_t i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);
                } else {
                    maxLength = std::max<int>(maxLength, i - stk.top());
                }
            }
        }
        return maxLength;
    }
};