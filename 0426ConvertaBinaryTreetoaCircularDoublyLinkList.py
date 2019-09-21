#User function Template for python3
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
# head=None
# pre = None

def bTreeToClist(root):
    #Your code here
    
    #Solution 3 divide and conque
    def connect(first, second):
        if not first:
            return second
        if not second:
            return first
        
        tail1 = first.left
        tail2 = second.left
        tail1.right = second
        second.left = tail1
        
        tail2.right = first
        first.left = tail2
        return first
    
    if not root:
        return
    left = bTreeToClist(root.left)
    right = bTreeToClist(root.right)
    root.left= root
    root.right = root
    return connect(connect(left, root), right)
    
    
    
    
    
    #Solution 2 inorder traverse
    # if not root:
    #     return None
    # def inorder(root, pre, head):
    #     if not root:
    #         return
    #     inorder(root.left, pre, head)
    #     if not head[0]:
    #         head[0]=root
    #         pre[0]=root
    #     else:
    #         root.left = pre[0]
    #         pre[0].right = root
    #         pre[0]=root
    #     inorder(root.right, pre, head)
        
    # pre =[None]
    # head = [None]
    # inorder(root, pre, head)
    # pre[0].right = head[0]
    # head[0].left = pre[0]
    # return head[0]
    
    
    #Solution 1 iteratively
    # if not root:
    #     return None
    # head = None
    # pre = None
    # stack = []
    # #stack.append(root)
    # while root or stack:
    #     while root:
    #         stack.append(root)
    #         root = root.left
    #     root =stack.pop()
    #     if not head:
    #         head = root
    #         pre = root
    #     else:
    #         pre.right = root
    #         root.left = pre
    #         pre=root
    #     root= root.right
    # head.left = pre
    # pre.right = head
    # return head
