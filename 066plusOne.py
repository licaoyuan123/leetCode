class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in range(len(digits)):
            # res+= digits[i] *pow(10, len(digits)-i-1)
            res= res*10+digits[i]
        return [int(i) for i in str(res+1)]
        
        
        # if digits[-1]!=9:
        #     digits[-1]+=1
        #     return digits
        # else:
        #     digits[-1] = 0
        #     digits[0:-1]= self.plusOne(digits[0:-1])
        #     return digits
        
