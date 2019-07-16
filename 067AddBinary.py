class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = len(a)-len(b)
        if diff>0:
            b= '0'*diff +b
        if diff<0:
            a = '0'* (-diff) +a
        
        l = len(a)-1
        curry = 0
        result=""
        while l>=0:
            s = int(a[l])+int(b[l]) +curry
            if s==3:
                
                curry=1
                result= "1" + result
            elif s==2:
                curry=1
                result= "0"+ result
            else:
                curry=0
                result=str(s)+ result            
            l-=1
        if curry:
            result= '1'+result
        return result
        
        
        
#         if len(a)==0:
#             return b
#         if len(b)==0:
#             return a
        
#         if a[-1]=='1' and b[-1]=='1':
#             return self.addBinary(self.addBinary(a[0:-1], b[0:-1]) ,'1')+'0'
#         if a[-1]=='0' and b[-1]=='0':
#             return self.addBinary(a[0:-1], b[0:-1])+'0'
#         else:
#             return self.addBinary(a[0:-1], b[0:-1])+'1'
        
        
#         M, N = len(a), len(b)
#         result ="".join( [0]*(max(M, N)+1))
        
#         shorter  =min(M,N)-1
#         last = len(result)-1
#         for i in xrange(shoter, -1, -1):
#             result[shorter] +=  
            
#             last-=1
        
        
            
            
        
