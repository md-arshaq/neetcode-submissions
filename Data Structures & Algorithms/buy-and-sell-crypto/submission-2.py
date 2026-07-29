class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0

        i = 1
        j = 0

        while(i<len(prices)):
            if prices[i]>prices[j]:
                maxprof = max(maxprof,prices[i]-prices[j])
            else:
                j=i
            i+=1
        
        return maxprof
