class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"M":1000, "D":500, "C": 100, "L":50, "X":10, "V":5, "I":1}
        #numList=[1000, 500, 100, 50, 10, 5, 1]
        total = 0
        for i in range(len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                total-=dic[s[i]]
            else:
                total+=dic[s[i]]
        total+=dic[s[-1]]            
            
        return total
        
