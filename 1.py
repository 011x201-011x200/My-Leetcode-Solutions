"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for enum1, num in enumerate(nums):
            for enum2, num2 in enumerate(nums[:enum] + nums[enum+1:]):
                if enum1 == enum2:
                    continue
                if num + num2 == target:
                    return  [enum1, enum2]