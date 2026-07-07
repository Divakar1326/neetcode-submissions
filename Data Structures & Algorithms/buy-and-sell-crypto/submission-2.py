class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day=prices[0]
        maxP=0
        for i in range(len(prices)):
                maxP=max(maxP,prices[i]-day)
                day=min(day,prices[i])
        return maxP 
        
        