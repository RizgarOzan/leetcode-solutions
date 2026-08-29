# 704. Binary Search (Easy)
# https://leetcode.com/problems/binary-search/
#
# Approach: classic binary search on a sorted array. Halve the search
# range until the target is found or the range is empty.
# O(log n) time, O(1) space.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
