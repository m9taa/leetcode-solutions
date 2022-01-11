#include <algorithm>
#include <vector>
#include <queue>


class NestedInteger {
  public:
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const std::vector<NestedInteger> &getList() const;
};


class NestedIterator {
// Time:  O(n)
// Space: O(n)
public:
    NestedIterator(const std::vector<NestedInteger> &nestedList) {
        flatten(nestedList);
    }
    
    int next() {
        int value = data.front();
        data.pop();
        return value;
    }
    
    bool hasNext() {
        return !data.empty();
    }
private:
    std::queue<int> data;
    void flatten(const std::vector<NestedInteger> &nestedList) {
        for (const auto& element: nestedList) {
            if (element.isInteger()) {
                data.push(element.getInteger());
            } else {
                flatten(element.getList());
            }
        }
    }
};
