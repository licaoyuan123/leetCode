class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #Iterative
        if n<0:
            x = 1/x
            n=-n
        result=1
        while n:
            if n & 1:
                result*=x
            n>>=1
            x*=x
        return result
            
        
        
        #Recursive
        # if not n:
        #     return 1
        # if n<0:
        #     x= 1/x
        #     n=-n
        #     return self.myPow(x, n)
        # if n%2:
        #     return x*self.myPow(x, n-1)
        # return self.myPow(x*x, n/2)
        
       
