# 136. Single Number (Easy)
# https://leetcode.com/problems/single-number/
#
# Approach: XOR everything together. A value XORed with itself is 0 and
# XOR with 0 leaves a value untouched, so every pair cancels out and the
# element that appears once is what remains. Order does not matter because
# XOR is commutative. O(n) time, O(1) space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
