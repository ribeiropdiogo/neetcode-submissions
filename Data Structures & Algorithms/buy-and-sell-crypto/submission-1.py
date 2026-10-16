class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        b, s = 0, 1

        while s < len(prices):
            print(b,s)
            if prices[s] > prices[b]:
                maxprofit = max(maxprofit,prices[s] - prices[b])
            else:
                b = s
            s += 1
        return maxprofit
        
            


        