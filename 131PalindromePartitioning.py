class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if isPar(s[:i]):
                    #path.append(s[:i])
                    dfs(s[i:], path+[s[:i]], res )
        def isPar(s):
            return s==s[::-1]
        res= []
        dfs(s,[], res)
        return res
