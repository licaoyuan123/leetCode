class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s[-1]==" ":
        #     return 0
        words = s.split(" ")
        cur = len(words)-1
        while cur>=0 and len(words[cur])==0:
            cur-=1
        
        return len(words[cur])
        
