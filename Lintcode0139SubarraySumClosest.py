#prefix_sum, after sorted, then we can find the minimum difference between elements, or we have to compare O(n**2) times.
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        prefix_sum = [(0, -1)]
        for i in range(len(nums)):
            prefix_sum.append((prefix_sum[-1][0]+nums[i], i ))
        prefix_sum.sort()
        minimum = float("inf")
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i][0]- prefix_sum[i-1][0]<minimum:
                minimum = prefix_sum[i][0]- prefix_sum[i-1][0]
                left = min(prefix_sum[i][1], prefix_sum[i-1][1])+1
                right = max(prefix_sum[i][1], prefix_sum[i-1][1])
        return left, right
