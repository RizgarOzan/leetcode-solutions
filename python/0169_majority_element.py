# 169. Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
#
# Approach: Boyer-Moore voting. Keep a candidate and a counter. A matching
# value bumps the counter, a different one cancels it out, and an empty
# counter means the next value becomes the new candidate. Since the
# majority element appears more than n/2 times it survives every
# cancellation. O(n) time, O(1) space.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
