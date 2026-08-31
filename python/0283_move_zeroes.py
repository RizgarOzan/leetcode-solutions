# 283. Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/
#
# Approach: two pointers. Walk the list and copy every non-zero value to
# the front, tracking where the next one goes. Everything after that
# position must be zeros, so fill it in.
# O(n) time, O(1) space.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slot = 0
        for num in nums:
            if num != 0:
                nums[slot] = num
                slot += 1
        for i in range(slot, len(nums)):
            nums[i] = 0
