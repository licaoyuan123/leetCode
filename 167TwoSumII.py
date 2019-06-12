class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        
        while left<right:
            total = numbers[left]+numbers[right]
            if total==target:
                break
            else:
                if total > target:
                    right-=1
                else:
                    left+=1
        return [left+1, right+1]
        
