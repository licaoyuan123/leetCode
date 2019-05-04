class Solution(object):
    def __init__(self):
        self.dic = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        #My Initial solution, however, Time Limit Exceeded(TLE)
        # if n==1:
        #     return 1
        # else:
        #     if n==2:
        #         return 2
        #     else:
        #         return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        #Solution 2, make a stack by my self, 28ms
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # result = 0
        # step=3
        # r1= 1
        # r2=2
        # while step<=n:
        #     result = r1+r2
        #     r1=r2
        #     r2=result            
        #     step+=1
        # return result
        #Third and fourth solution are the similar speed and space cost
        #solution 3 use array or hashmap to memorize
        # steps=[]
        # steps.append(1)
        # steps.append(2)
        # if n>2:
        #     for x in xrange(3,n+1):
        #         steps.append(steps[x-3]+steps[x-2])
        # print(steps)
        # return steps[n-1]
        
        #solution 4 use dict
        for x in xrange(1,n+1):
            if x not in self.dic:
                self.dic[x]=self.climbStairs(x-1)+self.climbStairs(x-2)
        return self.dic[n]
        
