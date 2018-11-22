class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profile=0
        for i in xrange(1, len(prices)):
            if prices[i]> prices[i-1]:
                max_profile+= prices[i]- prices[i-1]
        return max_profile
        
        # if len(prices)<=1:
        #     return 0
        # i,max_profit=0,0
        # valley=prices[0]
        # peak=prices[0]
        # while i< len(prices)-1:
        #     while i< len(prices)-1 and prices[i]>= prices[i+1]:
        #         i+=1
        #     valley= prices[i]
        #     while i< len(prices)-1 and prices[i]<=prices[i+1]:
        #         i+=1
        #     peak= prices[i]
        #     max_profit+= peak-valley
        # return max_profit
        
        
        
        
        # for i,value in enumerate(prices):
        #     if
#         benefit=0
#         for i in range(len(prices)-1):
#             if prices[i+1]>i:
#                 benefit += prices[i+1]-prices[i]
                
#         return benefit

