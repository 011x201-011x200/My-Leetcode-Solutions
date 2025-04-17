"""119. Pascal's Triangle II
Easy
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        for row in range(rowIndex+1):
            sub = []
            for i in range(len(ret) + 1):
                if i == 0 or i == row:
                    sub.append(1)
                else:
                    sub.append(ret[i-1]+ret[i])
            ret = sub
        return ret