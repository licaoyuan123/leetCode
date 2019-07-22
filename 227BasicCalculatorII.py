class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        num,stack, sign =0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i]) 
            if s[i] in "+-*/" or i==len(s)-1:
            #if (not s[i].isspace() and not s[i].isdigit()) or i==len(s)-1:
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="*":
                    stack.append(stack.pop()*num)
                else:
                    l= stack.pop()
                    if l>0:
                        stack.append(l/num)
                    else:
                        stack.append(-(-l/num))
                num=0
                sign = s[i]
            #print(stack)
        return sum(stack)
        
