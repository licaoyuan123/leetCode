class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        pre = [1,1]
        for k in range(2, rowIndex+1):
            cur= [1]*(k+1)
            for j in range(1, k):
                cur[j] = pre[j-1]+pre[j]
            pre = cur
        return pre
        
