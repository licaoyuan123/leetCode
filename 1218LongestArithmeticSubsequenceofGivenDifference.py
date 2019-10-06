class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        dp=[1]*N
        dic={}
        #dic[arr[0]] = 1
        for i in range(N):
            if arr[i]-difference in dic:
                dic[arr[i]] = dic[arr[i]-difference]+1
            else:
                dic[arr[i]] = 1
        result= -float("inf")
        # for ele in arr:
        #     if ele in dic and dic[ele]>result:
        #         result = dic[ele]
        #return max(dic, key=dic.get)
        return max(dic.values())   
