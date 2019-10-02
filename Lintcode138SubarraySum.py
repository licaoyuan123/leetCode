class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic={0:-1}
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum+=nums[i]
            if pre_sum in dic:
                return dic[pre_sum]+1, i
            dic[pre_sum] = i
        return -1, -1
