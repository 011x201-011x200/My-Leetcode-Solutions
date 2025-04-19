"""338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."""

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        sub = [1, 2]
        ret = [0, 1, 1, 2]
        while n+1 > len(ret):
            if n > 3:
                sub = sub + [i+1 for i in sub]
                ret.extend(sub)
        while len(ret) - 1 > n:
            ret.pop()
        return ret
    
