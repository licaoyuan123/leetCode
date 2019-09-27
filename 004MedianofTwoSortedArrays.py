class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N=len(nums1)+len(nums2)
        if N%2==1:
            return self.findKth(nums1, 0, nums2, 0, N//2+1)
        else:
            return (self.findKth(nums1, 0, nums2, 0, N//2)+self.findKth(nums1, 0, nums2, 0, N//2+1)  )/2
        
    def findKth(self, nums1, index1, nums2, index2, k):
        if index1==len(nums1):
            return nums2[index2+k-1]
        if index2==len(nums2):
            return nums1[index1+k-1]
        if k==1:
            return min(nums1[index1], nums2[index2])
        a = nums1[index1+k//2-1] if index1+k//2<=len(nums1) else None
        b = nums2[index2+k//2-1] if index2+k//2<=len(nums2) else None
        
        if b==None or (a!=None and a<b):
            return self.findKth(nums1, index1+k//2, nums2, index2, k-k//2)
        else:
            return self.findKth(nums1, index1, nums2, index2+k//2, k-k//2)
        
        
        
        # m=len(nums1)
        # n=len(nums2)
        # if m>n:
        #     nums1, nums2, m, n = nums2, nums1, n, m
        # half_length = (m+n+1)//2
        # imin, imax= 0, m
        # while imin<=imax:
        #     i=(imin+imax)//2
        #     j = half_length -i
        #     if i>0 and nums1[i-1]>nums2[j]:
        #         imax= i-1
        #     elif i<m and nums1[i]<nums2[j-1]:
        #         imin = i+1
        #     else:
        #         #Correct
        #         if i==0:
        #             max_left = nums2[j-1]
        #         elif j==0:
        #             max_left = nums1[i-1]
        #         else:
        #             max_left  = max(nums1[i-1], nums2[j-1])
        #         if (m+n)%2==1:
        #             return max_left
        #         else:
        #             if i==m:
        #                 min_right = nums2[j]
        #             elif j==n:
        #                 min_right = nums1[i]
        #             else:
        #                 min_right = min(nums1[i], nums2[j])
        #         return (max_left+min_right)/2 
                    
        
