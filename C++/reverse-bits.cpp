#include <cstdint>


class Solution {
public:
    std::uint32_t reverseBits1(std::uint32_t n) {
        // Time : O(1)
        // Space: O(1)
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
    }

    std::uint32_t reverseBits2(std::uint32_t n) {
        // Time : O(32)
        // Space: O(1)
        std::uint32_t result = 0;
        std::uint8_t power = 31;
        while (n != 0) {
            result += (n & 1) << power;
            power--;
            n >>= 1;
        }
        return result;
    }
};