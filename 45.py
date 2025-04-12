"""45. Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        def bestJump(lst, index):
            if index >= len(lst)-1:
                return -1
            else:
                cand = 1
                for i in range(1, min(lst[index] + 1, len(lst)-index)):
                    if lst[index + i] + i >= lst[index + cand] + cand or i+index >= len(lst)-1:
                        cand = i
                return index+cand
        index = 0
        jumps = 0
        while index >= 0:
            index = bestJump(nums, index)
            jumps += 1
        return jumps - 1
