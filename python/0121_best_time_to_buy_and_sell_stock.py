# 121. Best Time to Buy and Sell Stock (Easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Approach: one pass, track the lowest price seen so far and the best
# profit if we sold today. O(n) time, O(1) space.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best:
                best = price - min_price
        return best
