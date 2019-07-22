class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12 or len(s)<4:
            return
        def dfs(s, index, path, result):
            if index==4:
                if not s:
                    result.append(path[:-1])
                return
            for i in range(1,4):
                if i<=len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], index+1, path+s[:i]+".", result)
                    if s[0] == "0":  # here should be careful 
                        break
                    
                    # if i==1:
                    #     dfs(s[i:], index+1, path+s[:i]+".", result)
                    # elif i==2 and s[0]!="0":
                    #     dfs(s[i:], index+1, path+s[:i]+".", result)
                    # elif i==3 and s[0]!="0" and int(s[:i])<256:
                    #     dfs(s[i:], index+1, path+s[:i]+".", result)
        result = []
        dfs(s, 0, "", result)
        return result
                    
        
#         if len(s)>12:
#             return
#         def dfs(s, index, path, result):
#             if index>=len(s):
#                 if len(path)!=4:
#                     return
                    
#                 for i in path:
#                     if int(i)>255:
#                         return
#                     if (len(i)>1 and i[0]=="0"):
#                         return
                    
#                 result.append(".".join(path))
#                 return 
#             for j in range(1,4):
#                 if index+j>len(s):
#                     break
#                 p = path +[s[index:index+j]]
#                 dfs(s, index+j, p, result)
                 
#         result=[]
#         dfs(s, 0, [], result)
#         return result
