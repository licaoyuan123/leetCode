class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        #N= len(arrays)
        # while len(arrays)!=1:
        #     N = len(arrays)
        #     newArrays = []
        #     for i in range(0, N, 2):
        #         if i==N-1:
        #             newArray = arrays[i]
        #         else:
        #             newArray = self.mergeTwoSortedArrays(arrays[i], arrays[i+1])
        #         newArrays.append(newArray)
        #     arrays = newArrays
        # return arrays[0]
        if not arrays:
            return []
        N = len(arrays)-1
        return self.helper(arrays, 0, N)
    def helper(self, arrays, start, end):
        if start==end:
            return arrays[start]
        if end-start==1:
            return self.mergeTwoSortedArrays(arrays[start], arrays[end])
        middle = start+(end-start)//2
        #left = self.helper(arrays, 0, middle)
        #right = self.helper(arrays, middle+1, end)
        return self.mergeTwoSortedArrays(self.helper(arrays, start, middle), self.helper(arrays, middle+1, end))
        
            
    def mergeTwoSortedArrays(self, nums1, nums2):
        if not(nums1 and nums2):
            return nums1 or nums2
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        #i, j=0, 0
        i=0
        j=0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        if i!=n1:
            for k in range(i, n1):
                result.append(nums1[k])
        if j!=n2:
            for k in range(j, n2):
                result.append(nums2[k])
        return result
