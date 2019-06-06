class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices)==0 or len(prices)==1:
            return 0
        prof = [0] * len(prices)
        mini = max(prices)
        print(mini)
        for i in range(0, len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            prof[i]= max(0, prices[i]- mini)
        
        return max(prof)
        
