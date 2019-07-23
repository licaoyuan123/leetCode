class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if not s:
        #     return ""
        s= list(s)
        
        left, right = 0, len(s)-1
        vow=set("AEIOUaeiou")
        while left<=right:
            while left<=right and s[left] not in vow:
                left+=1
            while left<=right and s[right] not in vow:
                right-=1
            if left>right:
                break
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return "".join(s)
            
            
        
#         if not s:
#             return ""
#         left= 0
#         right = len(s)-1
#         result = [""]*len(s)
#         while left<=right:
#             while left<=right:
#                 if not s[left] in "AEIOUaeiou":
#                     result[left] = s[left]
#                     left+=1
                    
#                 else:
#                     break
#             while left<=right:
#                 if not s[right] in "AEIOUaeiou":
#                     result[right]=s[right]
#                     right-=1
#                 else:
#                     break
#             if left<=right:
#                 #temp= s[left]
#                 result[left]=s[right]
#                 result[right] = s[left]
#                 left+=1
#                 right-=1
#         return "".join(result)
            
                
