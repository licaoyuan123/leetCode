#Use the trick that for i in range(1, 1) will neve be executed

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #Soultion0
        res = [[1]*n for n in range(1, numRows+1) ]
        for i in range(1, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1]+ res[i-1][j] 
        return res
        
        
        #My solution, solved the problem however it a little bit too complicated
        # pre= [1]
        # res= []
        # res.append(pre)
        # if numRows==0:
        #     return []
        # if numRows==1:
        #     return res
        # for i in range(1, numRows):
        #     row = [0]*(i+1)
        #     row[0] = pre[0]
        #     row[-1] = pre[-1]
        #     for j in range(1, len(row)-1):
        #         row[j] = pre[j-1]+pre[j]
        #     res.append(row)
        #     pre = row
        # return res
            
            
        
