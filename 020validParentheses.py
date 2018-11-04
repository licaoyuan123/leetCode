class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic= {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c  not in dic:
                stack.append(c)
            elif not stack or dic[c]!= stack.pop():
                    return False
        return not stack
