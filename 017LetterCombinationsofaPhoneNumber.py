class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        ma= {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        res = []
        
        
        self.dfs(digits, ma,0, "", res)
        
        return res
        
        
    def dfs(self, st, ma,index,  path, res):
        if len(path)==len(st):
            res.append(path)
            return
            
        for j in range(len(ma[st[index]])):
            self.dfs(st, ma,index+1, path+ma[st[index]][j], res)
        
