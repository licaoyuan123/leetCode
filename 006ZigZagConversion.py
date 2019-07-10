class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows>len(s) or numRows==1:
            return s
        index, step = 0, 1
        L = [""]*numRows
        for ch in s:
            L[index]+=ch
            if index==0:
                step=1
            if index==numRows-1:
                step=-1
            index+=step
            
        return "".join(L)
