class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used={}
        start, ans=0, 0
        for index, ch in enumerate(s):
            if ch in used and start<=used[ch]:
                start=used[ch]+1
            else:
                ans = max(ans, index-start+1)
            used[ch] = index
        return ans
                
        
        
        # n= len(s)
        # ans = 0
        # m={}
        # i=0
        # for j in range(n):
        #     if s[j] in m:
        #         i= max(i, m[s[j]]+1)
        #     ans= max(ans, j-i+1)
        #     m[s[j]] = j
        # return ans
        
        
        #Solution 1 using sliding window
#         n = len(s)
#         se = set()
#         ans , i, j= 0, 0, 0
#         while i<n and j<n:
#             if not s[j] in se:
#                 se.add(s[j])
#                 j+=1
#                 ans =max(ans, j-i)
#             else:
#                 se.remove(s[i])
#                 i+=1
#         return ans
        
        
        #Solution 0: Bruce How ever TLE
#         def allUnique(s, start, end):
#             se =set()
#             for i in range(start, end):
#                 ch = s[i]
#                 if ch in se:
#                     return False
#                 se.add(ch)
#             return True
        
#         longest =0
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 if(allUnique(s, i, j)):
#                     longest = max(longest, j-i)
#         return longest
         
            
        
