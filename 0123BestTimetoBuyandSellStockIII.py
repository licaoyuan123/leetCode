class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Expand K
        N= len(prices)
        if N<2:
            return 0
        buy1=buy2=float("inf")
        sell1=sell2=0
        for i in range(N):
            buy1=min(prices[i], buy1)
            sell1=max(sell1, prices[i]-buy1)
            buy2=min(buy2, prices[i]-sell1)
            sell2=max(sell2, prices[i]-buy2)
        return sell2
        #Compact one dimension
        N= len(prices)
        K=2
        if N<2:
            return 0
        max_diff_vec=[-prices[0]]*(K+1)
        dp=[0]*(K+1)
        for i in range(1, N):
            for k in range(1, K+1):
                max_diff_vec[k]=max(dp[k-1]-prices[i], max_diff_vec[k])
                dp[k]=max(dp[k], max_diff_vec[k]+prices[i])
        return dp[K]
        
        
        #Swap two fors
        N= len(prices)
        K=2
        if N<2:
            return 0
        max_diff_vec=[-prices[0]]*(K+1)
        dp=[[0]*N for i in range(K+1)]
        for i in range(1, N):
            #max_diff=-prices[0]
            for k in range(1, K+1):
                max_diff_vec[k]=max(dp[k-1][i-1]-prices[i], max_diff_vec[k])
                dp[k][i]=max(dp[k][i-1], max_diff_vec[k]+prices[i])
        return dp[K][N-1]  
        
        
        #O(KN) Observation and find the repeated part and then 
        #make optimization
        N= len(prices)
        K=2
        if N<2:
            return 0
        dp=[[0]*N for i in range(K+1)]
        for k in range(1, K+1):
            max_diff=-prices[0]
            #max_diff=0
            for i in range(1, N):
                max_diff=max(dp[k-1][i-1]-prices[i], max_diff)
                # if i>1:
                #     max_diff=max(dp[k-1][i-2]-prices[i-1], max_diff)
                dp[k][i]=max(dp[k][i-1], max_diff+prices[i])
        return dp[K][N-1]  
        
        
        
        
        #O(KN^2)
        N= len(prices)
        K=2
        if N<2:
            return 0
        dp=[[0]*N for i in range(K+1)]
        for k in range(1, K+1):
            for i in range(1, N):
                max_diff=0
                for j in range(i):
                    max_diff=max(dp[k-1][j]-prices[j]+prices[i], max_diff)
                dp[k][i]=max(dp[k][i-1], max_diff)
        return dp[K][N-1]
                        
                    




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
        
 
