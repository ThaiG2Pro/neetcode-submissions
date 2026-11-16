class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        profix=0
        while r < len(prices):
            if prices[l] > prices[r] :
                l=r
                continue
            profix=max(profix, prices[r]-prices[l])
            r+=1
        return profix
            