# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.index=0
        self.result=[]
        if not root:
            return None
        
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            self.result.append(root.val)
            root=root.right
            
            
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.index+=1
            return self.result[self.index-1]
        return None
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index<len(self.result)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
