#LEETCODE 121 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit=float("inf")
        max_profit=0
        for i in prices:
            min_profit=min(min_profit,i)
            profit=i-min_profit
            max_profit=max(max_profit,profit)
        return max_profit
        #TC=O(n)
        #SC=O(1)
