#import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue= collections.deque()
        # self.first = queue.Queue()
        # self.second=queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
            
        # if self.first:
        #     self.first.put(x)
        # else:
        #     self.second.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.popleft()
        # if self.first:
        #     for _ in range(self.first.qsize()-1):
        #         self.second.put(self.first.get())
        #     return self.first.get()
        # elif self.second:
        #     for _ in range(self.second.qsize()-1):
        #         self.first.put(self.second.get())
        #     return self.second.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]
        # if not self.first and not self.second:
        #     return None
        # if self.first:
        #     for _ in range(self.first.qsize()):
        #         temp = self.second.put(self.first.get())
        #     return temp
        # elif self.second:
        #     for _ in range(self.second.qsize()-1):
        #         temp = self.first.put(self.second.get())
        #     return temp
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue)==0:
            return True
        else:
            return False
        # if not self.first and not self.second:
        #     return True
        # else:
        #     return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
