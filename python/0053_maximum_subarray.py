# 53. Maximum Subarray (Medium)
# https://leetcode.com/problems/maximum-subarray/
#
# Approach: Kadane's algorithm. Walk the array keeping the best sum of a
# subarray that ends at the current index. Extending the previous one only
# helps while its sum is positive, otherwise it is better to start over
# from the current value. The answer is the largest of those running sums.
# O(n) time, O(1) space.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best
