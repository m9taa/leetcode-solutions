class Solution {
public:
    int fib(int n) {
        // Time:  O(n)
        // Space: O(1)
        int prev = 0, current = 1;
        for (int i = 0; i < n; i++) {
            int tmp = prev;
            prev = current;
            current += tmp;
        }
    return prev;
    }
};