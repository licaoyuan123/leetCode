class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Solution3
        if not nums:
            return 0
        nums.sort()
        left = nums[0]
        temp =1
        best = 0
        for num in nums:
            if num==left:
                continue
            else:
                if num-left==1:
                    temp+=1
                    best = max(best, temp)
                else:
                    temp = 1
            left = num
        best = max(best, temp)
        return best
                
        
        
        
        #solution2 time complex is O(n) each time delete one entry
        # dic={}
        # for num in nums:
        #     dic[num] =1
        # best = 0
        # for num in nums:
        #     if num in dic:
        #         len=1
        #         del dic[num]
        #         left = num-1
        #         right = num+1
        #         while left in dic:
        #             del dic[left]
        #             left-=1
        #             len+=1
        #         while right in dic:
        #             del dic[right]
        #             right+=1
        #             len+=1
        #     best = max(best, len)
        # return best

        #Solution 1 use dic or set
        #worst case time complex is o(n**2)
        # all_nums = set(nums)
        # best = 0
        # for num in nums:
        #     x = num
        #     while x in all_nums:
        #         x+=1
        #     best = max(best, x-num)
        # return best
                
        
