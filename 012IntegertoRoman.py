class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Solution1 
        NUM = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nu = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4,1]
        res = ""
        for index, v in enumerate(nu):
            res+= (num/v)*NUM[index]
            num = num%v
        return res
        
        #Solution 0, smart trick
#         M= ["", "M", "MM", "MMM"]
#         C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#         X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
#         I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
#         return M[num/1000]+C[num%1000/100]+X[num%100/10]+I[num%10]
            
        
