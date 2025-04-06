"""88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # remove trailing zeros
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        # special cases
        if m == 0:
            nums1[:] = nums2[:]
            return
        elif n == 0:
            return
        if m == 1 and n == 1:
            nums1[:] = [min(nums1[0], nums2[0]), max(nums1[0], nums2[0])]
            return
        # merge lists
        k = 1
        for j in range(n):
            if nums2[j] <= nums1[0]:
                nums1[:] = [nums2[j]] + nums1[:]
                continue
            elif nums2[j] >= nums1[-1]:
                nums1[:] = nums1[:] + [nums2[j]]
                continue
            for i in range(k,len(nums1)):
                if nums1[i-1] < nums2[j]:
                    if nums1[i] >= nums2[j]:
                        nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:]
                        k = i
                        break