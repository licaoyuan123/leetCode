class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1:
            return 0
        half=pow(2, N-2)
        if K<=half:
            return self.kthGrammar(N-1, K)
        else:
            res = self.kthGrammar(N-1, K-half)
            if res:
                return 0
            else:
                return 1
        
        # if not N or N==1:
        #     return 0
        # # num=[0,1]*pow(2,N-1)
        # # return num[K-1]
        # pre=[0]
        # for i in range(2,N+1):
        #     cur = [0]*pow(2, i-1)
        #     cur[1]=1
        #     for index, p in enumerate(pre):
        #         if p:
        #             cur[pow(2, index)]=1
        #         else:
        #             cur[pow(2, index)-1]=1
        #     pre=cur
        # return pre[K-1]
        
