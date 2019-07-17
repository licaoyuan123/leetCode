class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0]*(len(s)+1)
        dp[0] =1
        for i in range(1, len(s)+1):
            if s[i-1]!='0':
                dp[i] += dp[i-1]
            
            if i!=1 and int(s[i-2])>0 and int(s[i-2:i])<27:
                dp[i] += dp[i-2]
        return dp[len(s)]
        # if s[0]=="0":
        #     return 0
        
#         result= []
#         path=[]
#         self.dfs(s, 0, path, result)
#         #print(result)
#         return len(result)
        
#     def dfs(self, s, index, path, result):
#         if index>len(s)-1 and path:
#             result.append(path)
#             return result
#         if int(s[index]):
#             path.append(s[index])
#             self.dfs(s, index+1, path, result)
#         else:
#             return
#         if index+1<len(s):
#             if not int(s[index:index+2]):
#                 return
            
#             if int(s[index:index+2])>26 or s[index]<1:
#                 return
#             else:
#                 path.append(s[index:index+2])
#                 self.dfs(s, index+2, path, result)
            
        
