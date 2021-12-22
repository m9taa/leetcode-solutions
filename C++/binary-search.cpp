#include <vector>


class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        // Time:  O(logn)
        // Space: O(1)
        if (nums.empty()) return -1;
        int start = 0;
        int end = nums.size();
        while (start + 1 < end) {
            int m = start + (end - start) / 2;
            if (nums[m] > target) {
                end = m;
            } else {
                start = m;
            }
        }
        return nums[start] == target? start : -1;
    }
};