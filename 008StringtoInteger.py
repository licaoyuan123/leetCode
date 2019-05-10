#Quite annoying, tried many times 
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ls =list(str.strip())
        if len(ls)==0:
            return 0
        sign = 1
        if len(ls) and ls[0] in {'+','-'}:
            if ls[0]=='-':
                sign=-1
            del ls[0]
        if len(ls)==0:
            return 0
        ret = 0
        for i in range(len(ls)):
            if ls[i].isdigit():
                ret = ret*10 + int(ls[i])
            else:
                return max(-2**31 ,min(sign* ret, 2**31-1))
        return max(-2**31 ,min(sign* ret, 2**31-1))
        
#         N = len(str)
#         if not N:
#             return 0
#         while(len(str) and str[0] ==' '):
#            str=str[1:]
#         # while(len(str) and (str[-1]<'0' or str[-1]>'9')):
#         #     str = str[0:-1]
#         flag=True
#         N = len(str)
#         if not N:
#             return 0
#         if str[0]=='-':
#             str=str[1:]
#             flag=False
#         if str[0]=='+':
#             str=str[1:]
#         i=0
#         while True:
#             if str[i]<'0' or str[i]>'9':
#                 str = str[0:i]
#             i+=1
#             if i>len(str)-1:
#                 break
        
        
#         N = len(str)
#         if not N:
#             return 0
        
#         if len(str)>10:
#             if flag:
#                 return 2147483647
#             else:
#                 return -2147483648
#         result = int(float(str))
#         if flag:
#             return result
#         else:
#             return -result
        
            
            

        
