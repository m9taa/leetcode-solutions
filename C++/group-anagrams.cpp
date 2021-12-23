#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <map>


class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(const std::vector<std::string>& strs) {
        // Time:  O(n)
        // Space: O(n)
        auto bag = std::map<std::string, std::vector<std::string>>();
        for (const std::string& s: strs) {
            std::string key = std::string(s);
            sort(key.begin(), key.end());
            bag[key].push_back(s);
        }
        std::vector<std::vector<std::string>> result = std::vector<std::vector<std::string>>();
        for (auto it: bag) {
            result.push_back(it.second);
        }
        return result;
    }
};