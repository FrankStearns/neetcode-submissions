class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            minprice = min(minprice, prices[i])
            profit = max(prices[i] - minprice, profit)
        return profit
            