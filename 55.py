"""55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def bestJump(lst, index):
            if index >= len(lst)-1:
                return -1
            elif lst[index] == 0:
                return -2
            else:
                cand = 1
                for i in range(1, min(lst[index] + 1, len(lst)-index)):
                    if lst[index + i] + i >= lst[index + cand] + cand:
                        cand = i
                return index+cand
        index = 0
        while index >= 0:
            index = bestJump(nums, index)
        return True if index == -1 else False
