class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0;right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1;right-=1
        return True
        # a=[]
        # for i in s:
        #     if i.isdigit() or i.isalpha():
        #         a.append(i.lower())
        # N = len(a)
        # half= N/2
        # if N%2==0:
        #     left= half-1
        #     right=half
        # else:
        #     left= half
        #     right=half
        # #print(a)
        # while left>=0 and right<N:
        #     if a[left]!=a[right]:
        #         return False
        #     else:
        #         left-=1
        #         right+=1
        # return True
        
        
