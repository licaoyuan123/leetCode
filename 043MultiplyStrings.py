class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        M, N=len(num1), len(num2)
        res= [0]*(M+N)
        
        last= len(res)-1
        for i in num1[::-1]:
            tempPos = last
            for j in num2[::-1]:
                first, second= int(i), int(j)
                res[tempPos] += first*second
                res[tempPos-1] += res[tempPos]/10
                res[tempPos] = res[tempPos]%10
                tempPos-=1
            last-=1
        cur= 0
        while cur<len(res)-1 and res[cur]==0:
            cur+=1
        result= "".join(map(str,res[cur:]))
        return result
        
