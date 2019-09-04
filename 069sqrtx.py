class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x
        while start+1<end:
            mid = start+(end-start)/2
            if mid**2 == x:
                return mid
            else:
                if mid**2>x:
                    end= mid
                else:
                    start = mid
        if end**2<=x:
            return end
        return start
        # for i in range(x/2+1):
        #     if i**2==x:
        #         return i
        #     if i**2<=x and (i+1)**2>x:
        #         return i
            
        



class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        
        l, r= 0,x
        
        while(l<=r):
            mid = (l+r)/2
            if mid**2==x:
                return mid
            if mid**2>x:
                r=mid-1
            else:
                if (mid+1)**2>x:
                    return mid
                l=mid+1
        
        
        #2147395599
        #Solution 1
        # temp = x/2
        # start=0
        # end =x
        # if x==1:
        #     return 1
        # while True:
        #     if temp**2>x:
        #         end=temp
        #     else:
        #         start=temp
        #         if (temp+1)**2>x:
        #             return temp
        #     temp = (start+end)/2
        # return temp
            
        # for i in range(x):
        #     if i**2<=x and (i+1)**2>x:
        #         return i
