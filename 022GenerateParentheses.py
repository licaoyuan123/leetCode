class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left, right = 0,0
        S = ""
        ans=[]
        def dfs(S, left, right, ans):
            if len(S)==2*n:
                ans.append(S)
                return
            if left<n:
                dfs(S+'(', left+1, right, ans)
            if right<left:
                dfs(S+")", left, right+1, ans)
        dfs(S, left, right, ans)
        return ans
