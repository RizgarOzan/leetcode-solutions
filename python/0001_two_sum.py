# 1. Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
#
# Approach: single pass with a hash map. For each number, check if its
# complement (target - num) was already seen. O(n) time, O(n) space.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
