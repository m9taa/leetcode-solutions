#include <vector>


class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        // Time:  O(n)
        // Space: O(1)
        int element = nums[0];
        int counter = 0;
        for (int num: nums) {
            if (counter == 0) {
                element = num;
                counter++;
            } else {
                if (num == element) {
                    counter++;
                } else {
                    counter--;
                }
            }
        }
        return element;
    }
};