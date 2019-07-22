class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1= [int(v) for v in version1.split(".")]
        s2 = [int(v) for v in version2.split(".")]
        
        for i in range(max(len(s1), len(s2))):
            n1= s1[i] if i<len(s1) else 0
            n2=s2[i] if i<len(s2) else 0
            if n1>n2:
                return 1
            if n1<n2:
                return -1
        return 0
        
        
        # s1 = version1.split(".")
        # s2 = version2.split(".")
        # for i in range(min(len(s1), len(s2))):
        #     if int(s1[i])>int(s2[i]):
        #         return 1
        #     elif int(s1[i]) < int(s2[i]):
        #         return -1
        # if len(s1)==len(s2):
        #     return 0
        # elif len(s1)>len(s2):
        #     larger = len(s1)-len(s2)
        #     for i in range(len(s2), len(s1)):
        #         if int(int(s1[i]))>0:
        #             return 1
        # else:
        #     for j in range(len(s1), len(s2)):
        #         if int(s2[j])>0:
        #             return -1
        # return 0
        
