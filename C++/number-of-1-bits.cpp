#include <cstdint>


class Solution {
public:
    int hammingWeight(std::uint32_t n) {
        // Time:  O(1)
        // Space: O(1)
        int result = 0;
        while (n != 0) {
            result += (n & 1);
            n >>= 1;
        }
        return result;
    }
};