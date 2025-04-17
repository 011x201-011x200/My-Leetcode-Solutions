"""118. Pascal's Triangle

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for row in range(numRows):
            sub = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    sub.append(1)
                else:
                    sub.append(ret[row-1][i-1]+ret[row-1][i])
            ret.append(sub)
        return ret