class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.firstIn = []
        self.firstOut = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.firstIn.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        self.out()
        return self.firstOut.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
       # if(not self.firstOut):
        self.out()
        return self.firstOut[-1]
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        #self.out()
       # if(len(firstOut)==0)
        
        return not self.firstOut and not self.firstIn
    def out(self):
        if(not self.firstOut):
            while(self.firstIn):
                self.firstOut.append(self.firstIn.pop())
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
