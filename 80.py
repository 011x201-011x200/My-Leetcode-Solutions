"""80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            j = i + 1
            k = 0
            while j <= len(nums) - 1:
                if nums[i] == nums[j]:
                    k+=1
                else:
                    break
                j+=1
            if k != 0:
                nums[:] = nums[:i+2] + nums[i+1+k:]
            i+=1
        return len(nums)
        