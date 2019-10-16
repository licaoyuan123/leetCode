#Add three pointers
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        i2, i3, i5 = 0, 0, 0
        while n>1:
            u2, u3, u5 = 2*dp[i2], 3*dp[i3], 5*dp[i5]
            mini = min(u2, u3, u5)
            if mini==u2:
                i2+=1
            if mini==u3:
                i3+=1
            if mini==u5:
                i5+=1
            dp.append(mini)
            n-=1
        return dp[-1]
