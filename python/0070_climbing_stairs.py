# 70. Climbing Stairs (Easy)
# https://leetcode.com/problems/climbing-stairs/
#
# Approach: the number of ways to reach step n is the sum of the ways to
# reach n-1 and n-2, so it is just Fibonacci. Keep only the last two
# values instead of a whole table.
# O(n) time, O(1) space.

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr
