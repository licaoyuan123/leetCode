class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""
        if not strs:
            return pre
        strs.sort()
        st= strs[0]
        for i, ch in enumerate(st):
            for others in strs:
                if others[i]!=ch:
                    return st[:i]
        return st
                
        
        
#         res = 0
#         n = len(strs)
#         ma= {}
#         for i in len(strs[0]):
#             ma[i] = strs[0][i] 
        
#         for i in range(1, len(strs)):
#             if strs
