class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        # N = len(chars)
        # if N==0 or N==1:
        #     return chars
        # left=0
        # right=N-1
        # while left<=right:
        #     while left<=right and chars[left].islower():
        #         left+=1
        #     while left<=right and chars[right].isupper():
        #         right-=1
        #     if left<=right:
        #         chars[left], chars[right] = chars[right], chars[left]
        #         left+=1
        #         right-=1
        # return chars
        return chars.sort(key=lambda c: c.isupper())
