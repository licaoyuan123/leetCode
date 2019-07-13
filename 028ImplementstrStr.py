class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L = len(needle)
        N = len(haystack)
        if N<L:
            return -1
        #print(haystack[2:4])
        for i in range(N-L+1):
            right= i+L
            if haystack[i:right]==needle: 
                return i
        return -1
            
