
#The second buy, cost price-first_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = float("inf")
        one_sell = 0
        two_buy = float("inf")
        two_sell = 0
        for i in range(len(prices)):
            p = prices[i]
            one_buy = min(one_buy, p)
            one_sell = max(one_sell, p-one_buy)
            
            two_buy = min(two_buy, p-one_sell)
            two_sell = max(two_sell, p-two_buy)
        return two_sell
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #My idea, calculate transaction once and twice
        #then get the maximum
        #transaction only once
        #How ever, the last test case Time Limit Exceeded
        if len(prices)<2:
            return 0
        profit_once = self.helper(prices, 0, len(prices)-1)
    
        profit_twice = 0
        for i in range(2, len(prices)-1):
            #for j in range(0, i):
            left= self.helper(prices, 0, i-1)
            right = self.helper(prices, i, len(prices)-1)
            profit_twice= max(profit_twice, left+right)
        print(profit_twice)
        return max(profit_once, profit_twice)
            
    def helper(self, prices, start, end):
        if start==end:
            return 0
        minimum = prices[start]
        profit_once = 0
        for i in range(start+1, end+1):
            profit_once = max(profit_once, prices[i]-minimum) 
            minimum = min(minimum, prices[i])
        return profit_once
        
 
