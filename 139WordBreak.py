class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp=[False]*(size+1)
        dp[0] = True
        for i in range(1, size+1):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i]==word:
                    dp[i]=True
        return dp[-1]
        
        
