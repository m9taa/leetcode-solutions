#include <vector>
#include <iostream>


class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int max_count = 2;
        int count = 1;
        int slow = 0;
        int fast = 1;
        while (fast < nums.size()) {
            if (nums[fast] == nums[slow]) {
                if (count < max_count) {
                    slow++;
                    nums[slow] = nums[fast];
                    count++;
                }
            } else {
                slow++;
                nums[slow] = nums[fast];
                count = 1;
            }
            fast++;
        }
        return slow + 1;
    }
};
