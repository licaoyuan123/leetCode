class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]
        self.min_stack = []
        self.minimum = float("inf")

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.minimum = min(self.minimum, x)
        self.min_stack.append(self.minimum)

    def pop(self) -> None:
        if len(self.nums)>0:
            self.nums.pop()
            self.min_stack.pop()
            self.minimum = self.getMin()
            if len(self.nums)==0:
                self.minimum = float("inf")
        else:
            return None
        

    def top(self) -> int:
        if len(self.nums)==0:
            return None
        return self.nums[-1]
    

    def getMin(self) -> int:
        if len(self.nums)==0:
            return None
        return self.min_stack[-1]
#Save some space:       
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]
        self.min_stack = []
        self.minimum = float("inf")

    def push(self, x: int) -> None:
        if len(self.nums)==0:
            self.nums.append(x)
            self.min_stack.append(x)
        
        else:
            if x<=self.min_stack[-1]:
                self.min_stack.append(x)
            self.nums.append(x)
        #self.minimum = min(self.minimum, x)
        

    def pop(self) -> None:
        if len(self.nums)>0:
            if self.nums[-1]==self.min_stack[-1]:
                self.min_stack.pop()
            self.nums.pop()
            #self.min_stack.pop()
            # self.minimum = self.getMin()
            # if len(self.nums)==0:
            #     self.minimum = float("inf")
        else:
            return None
        

    def top(self) -> int:
        if len(self.nums)==0:
            return None
        return self.nums[-1]
    

    def getMin(self) -> int:
        if len(self.nums)==0:
            return None
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
