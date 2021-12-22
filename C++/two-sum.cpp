#include <vector>
#include <map>


class Solution {
public:
    std::vector<int> twoSum(std::vector<int> nums, int target) {
        // Time:  O(n)
        // Space: O(n)
        std::vector<int> result;
        std::map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            auto it = m.find(diff);
            if (it != m.end()) {
                result = {it->second, i};
                break;
            } else {
                m[nums[i]] = i;
            }
        }
        return result;
    }
};