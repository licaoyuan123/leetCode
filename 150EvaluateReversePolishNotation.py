#I utilized stack to store operands
#Seems questions being easier and easier for me.
#To Rember: -3/2=-2   3/2=1  -int / int, the result will be trancated to -inf
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operand= []
        N = len(tokens)
        for i in range(N):
            if tokens[i] !='+' and tokens[i]!='-' and tokens[i]!="*" and tokens[i]!="/":
                operand.append(int(tokens[i]))
            else:
                second = operand.pop()
                first = operand.pop()
                if tokens[i]=="+":
                    operand.append(first + second)
                elif tokens[i]=="-":
                    operand.append(first - second)
                elif tokens[i]=="*":
                    operand.append(first * second)
                else:
                    if first*second <0:
                        operand.append(-(abs(first)/abs(second)))
                    else:
                        operand.append(first / second)
           # print(operand)
        return operand.pop()
    
    #                ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        
