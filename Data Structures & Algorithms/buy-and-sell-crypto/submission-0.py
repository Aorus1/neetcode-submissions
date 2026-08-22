class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        bestprofit = 0
        for i in range(1, len(prices)):
            bestprofit = max(bestprofit, prices[i] - minbuy)
            minbuy = min(prices[i], minbuy)


        return bestprofit