class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sellday=[0]*len(prices)
        maxP=0
        sellday[-1]=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            sellday[i]=max(sellday[i+1],prices[i])
        print(sellday)
        for j in range(len(prices)):
            if sellday[j]<=prices[j]:
                continue
            else:
                profit=sellday[j]-prices[j]
                maxP=max(maxP,profit)
        return maxP if maxP>0 else 0
        
        