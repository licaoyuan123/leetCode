# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Although the third version is clearly, the first solution is quicker.
        #However it use an external stack(list)
        #Third version with iterative more clearly
        prev =None
        while(head !=None):
            
            nextTemp = head.next
            head.next, prev, head = prev, head, nextTemp
            # head.next = prev
            # prev = head
            # head = nextTemp
        return prev
            
        
        #Second Recursive version
    #     return self._reverse(head)
    # def _reverse(self, node,prev=None):
    #     if not node:
    #         return prev
    #     nextNode = node.next
    #     node.next = prev
    #     return self._reverse(nextNode,node)
        
        
        
        #My first implemention with stack structure
        # cur = head
        # nodeList=[]
        # while cur.next != None:
        #     nodeList.append(cur)
        #     cur = cur.next
        # newHead = nodeList.pop()
        # current = newHead
        # for i in range(len(nodeList)):
        #     current.next = nodeList.pop()
        #     current = current.next
        # current.next = None
        
            
        #while current.next = nodeList.pop():
         #   current = current.next
       # current.next= NULL
            
            
        #return newHead

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
