"""121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cand_high = 0
        cand_low = prices[0] 
        max_profit = 0
        prev_profit = 0
        for enum, price in enumerate(prices[1:]):
            if price < cand_low and enum < len(prices)-2:
                cand_low = price
                cand_high = 0
            elif price > cand_high and max_profit < price - cand_low:
                cand_high = price
                if price - cand_low > prev_profit:
                    prev_profit = max_profit
                    max_profit = cand_high - cand_low
        return max_profit
