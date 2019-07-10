class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        ans = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            temp1 = self.helper(s, i, i+1)
            ans = max(temp, temp1,ans, key=len)
            # if len(temp)>len(ans):
            #     ans = temp
            # temp = self.helper(s, i, i+1)
            # if len(temp)>len(ans):
            #     ans = temp
        return ans
    def helper(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
      
                    
            
