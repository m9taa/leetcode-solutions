from typing import List


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> 'List[NestedInteger]':
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    # Time:  O(n)
    # Space: O(n)
    def __init__(self, nestedList: List[NestedInteger]):
        self.data = []
        self._flatten(nestedList)

    def _flatten(self, nestedList: List[NestedInteger]) -> None:
        for element in nestedList:
            if element.isInteger():
                self.data.append(element.getInteger())
            else:
                self._flatten(element.getList())

    def next(self) -> int:
        return self.data.pop(0)

    def hasNext(self) -> bool:
        return bool(self.data)
