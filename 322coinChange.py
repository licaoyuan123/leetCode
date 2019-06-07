class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount ==0:
            return 0
        MAX = float('inf')
        num=[0] + [MAX ]*amount
        
        for j in range(1, amount+1):
            num[j] =min([num[j-c] if j-c>= 0 else MAX for c in coins]  )+1 
        if num[amount]==MAX:
            return -1
        else:
            return num[amount]
      
        
     #num[]     
 # for i in coins:
        #     num[i] = 1        
#     if j in coins:
#                 num[j]= 1
#             else:
#                 num[j] = min([n if n in coins for n in range(1,n) ])+1
               
# #             cur=[]
#             for h in range(0, len(coins)):
#                 cur.append(num[h])
#             num[j] = min(cur)+1
#         return num[amount]
        
        
