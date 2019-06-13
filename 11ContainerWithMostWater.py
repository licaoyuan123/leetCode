class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #move toward the shorter line in each step
        
        if len(height)<2:
            return 0
        left,right, maxArea = 0, len(height)-1, 0
        while left<right:
            area =(right- left )*min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
                
            
        return maxArea
        
        
        
        
        #My first solution, however it is TLE
        #TLE
        # if len(height)<2:
        #     return 0
        # maxi = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         if (j-i)*min(height[i], height[j])>maxi:
        #             maxi = (j-i)*min(height[i], height[j])
        # return maxi
            
