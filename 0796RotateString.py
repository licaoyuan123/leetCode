class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A)!=len(B):
            return False
        for i in range(len(A)):
            A = A[1:] +A[:1]
            if A==B:
                return True
        return False
        
    #     if not A and not B:
    #         return True
    #     length_a =len(A)
    #     length_b = len(B)
    #     if length_a!=length_b:
    #         return False
    #     for i in range(1, length_a):
    #         target = self.rotate(A, i)
    #         if target==B:
    #             return True
    #     return False
    # def rotate(self, string, num):
    #     left=string[0:num]
    #     right = string[num:]
    #     result = right+left
    #     return result
        
