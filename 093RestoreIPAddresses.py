class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12:
            return
        def dfs(s, index, path, result):
            if index>=len(s):
                if len(path)!=4:
                    return
                    
                for i in path:
                    if int(i)>255:
                        return
                    if (len(i)>1 and i[0]=="0"):
                        return
                    
                result.append(".".join(path))
                return 
            for j in range(1,4):
                if index+j>len(s):
                    break
                p = path +[s[index:index+j]]
                dfs(s, index+j, p, result)
                 
        result=[]
        dfs(s, 0, [], result)
        return result
