# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Intution: Consider every day is selling price, and now find the minimum purchase price before that day, and calculate the profit. Keep track of the maximum profit.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        minPurchasePrice = prices[0]

        for value in prices:
            result = max(result, value - minPurchasePrice)

            minPurchasePrice = min(value, minPurchasePrice)

        return result