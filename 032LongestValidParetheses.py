class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Solution 0:
        #Use laststart to record the earlist validate '('
        laststart= -1
        stack=[]
        ans= 0
        for i in range(len(s)):
            if s[i]=='(':
                if laststart==-1:
                    stack.append(i)
                else:
                    stack.append(laststart)
                    laststart=-1
            else:
                if len(stack)!=0:
                    tempstart = stack.pop()
                    ans = max(ans, i-tempstart+1)
                    laststart= tempstart
                else:
                    laststart=-1
        return ans
        
        #Solution 1 use dp[i+1] to record the longest number until i 
        # N = len(s)
        # dp = [0]*(N+1)
        # stack=[]
        # for i in range(N):
        #     if s[i]=="(":
        #         stack.append(i)
        #     else:
        #         if stack:
        #             p = stack.pop()
        #             dp[i+1] = dp[p]+i-p+1
        # result = max(dp)
        # return result
                    
        
