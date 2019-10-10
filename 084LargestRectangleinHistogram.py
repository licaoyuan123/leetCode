#O(n) solution, use an extra acending stack, 
#each time pop the values smaller than current value,
#so we can get the first smaller value's index(left is the previous one, right is the current one)
#we use the stack to store index to calculate the width
#add -1 to the end to make sure each value is poped.


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #O(n) acending stack
        N=len(heights)
        if N==0:
            return 0
        stack = []
        cur=0
        max_area = 0
        for i in range(N+1):
            if i==N:
                cur = -1
            else:
                cur = heights[i]
            while len(stack)!=0 and cur<=heights[stack[-1]]:
                h = heights[stack.pop()]
                if len(stack)==0:
                    width = i
                else:
                    width=i-stack[-1]-1
                    
                area = h*width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
        
        
        #O(n**2) however, TLE
        # N = len(heights)
        # if N==0:
        #     return 0
        # max_area = -float("inf")
        # for i in range(N):
        #     left=-1
        #     right=N
        #     for j in range(i-1, -1, -1):
        #         if heights[j]<heights[i]:
        #             left=j
        #             break
        #     for k in range(i+1, N):
        #         if heights[k]<heights[i]:
        #             right=k
        #             break
        #     area=heights[i]*(right-left-1)
        #     max_area = max(max_area, area)
        # return max_area
