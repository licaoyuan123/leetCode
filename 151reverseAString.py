class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Solution 0 using swap to swap first and last
        l= s.split()
        start=0
        end = len(l)-1
        while start<end:
            temp=l[start]
            l[start]=l[end]
            l[end]=temp
            start+=1
            end-=1
        return (" ").join(l)
        
        
        #Solution1 usint stack to do the reverse
        # stack= s.split()
        # result=[]
        # while stack:
        #     result.append(stack.pop())
        # return (" ").join(str(x) for x in result)
        
        
    #I thought it is reverse each char    
#         for i in range(len(s)):
#             char= s.pop()
#             if char==' ':
#                 space+=1
#             else:
#                 space=0
            
#             if space<2:
#                 stack.append(char)
#         return stack
        
