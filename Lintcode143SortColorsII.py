
#Solution 2 O(nk)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        #colors.sort()
        count=0
        left=0
        right = len(colors)-1
        while count<k:
            minimum=float("inf")
            maximum = -float("inf")
            for i in range(left, right+1):
                minimum = min(minimum, colors[i])
                maximum = max(maximum, colors[i])
            cur=left
            while cur<=right:
                if colors[cur]==minimum:
                    colors[cur], colors[left] = colors[left], colors[cur]
                    cur+=1
                    left+=1
                elif colors[cur]==maximum:
                    colors[cur], colors[right] = colors[right], colors[cur]
                    right-=1
                else:
                    cur+=1
            count+=1
            
                
