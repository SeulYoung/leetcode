from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        m = len(prices)
        max_value = 0
        for i in range(m):
            for j in range(i, m):
                max_value = max(max_value, prices[j] - prices[i])
        return max_value

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price, max_profit = prices[0], 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
