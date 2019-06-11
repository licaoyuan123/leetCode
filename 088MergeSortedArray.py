class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n>0:
            nums1[0:n] = nums2[0:n]
        
        
        
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i-m]
        # while(0 in nums1):
        #     nums1.remove(0)
        
        

        
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i-m]
        # while(0 in nums1):
        #     nums1.remove(0)
        # nums1= sorted(nums1)
        # return
#        return sorted(nums1)
        
