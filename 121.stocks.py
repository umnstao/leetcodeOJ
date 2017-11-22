class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        lowest = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] - lowest > profit:
                profit = prices[i] - lowest
            if prices[i] < lowest:
                lowest = prices[i]
        return profit
