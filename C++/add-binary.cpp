#include <string>


class Solution {
public:
    std::string addBinary(std::string a, std::string b) {
        // Time:  O(n)
        // Space: O(n)
        size_t carry = 0;
        std::string result;

        for (auto a_it = a.rbegin(), b_it = b.rbegin(); a_it < a.rend() || b_it < b.rend();) {
            size_t a_i = (a_it != a.rend()) ? *a_it - '0' : 0;
            size_t b_i = (b_it != b.rend()) ? *b_it - '0' : 0;

            size_t residue = a_i + b_i + carry;
            carry = residue / 2;
            residue %= 2;
            result.push_back('0' + residue);

            if (a_it != a.rend()) {
                ++a_it;
            }
            if (b_it != b.rend()) {
                ++b_it;
            }
        }
        if (carry != 0) {
            result.push_back('0' + carry);
        }
        std::reverse(result.begin(), result.end());
        return result;
    }
};