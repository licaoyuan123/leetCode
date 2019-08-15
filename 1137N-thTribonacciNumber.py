class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """            
        # if n==0:
        #     return 0
        # if n<3:
        #     return 1
        # return self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
        
        
        result=[0]*(n+3)
        result[1]=1
        result[2]=1
        if n>2:
            for i in range(3,n+1):
                result[i]=result[i-3]+result[i-2]+result[i-1]
        
        return result[n]
        
