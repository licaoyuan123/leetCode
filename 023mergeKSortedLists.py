# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        while len(lists)>1:
            newLists = []
            for i in range(0, len(lists), 2):
                if i+1==len(lists):
                    newList =  lists[i]
                else:
                    newList =self.mergeTwoSortedLists(lists[i], lists[i+1])
                newLists.append(newList)
            lists = newLists
        return lists[0]
            
        
        return self.mergeKListsHelper(lists, 0, len(lists)-1)
    # def mergeKListsHelper(self,lists, start, end):
    #     if start==end:
    #         return lists[start]
    #     if end-start==1:
    #         return self.mergeTwoSortedLists(lists[start], lists[end])
    #     middle =start+(end-start)//2
    #     left = self.mergeKListsHelper(lists, start, middle)
    #     right = self.mergeKListsHelper(lists, middle+1, end)
    #     return self.mergeTwoSortedLists(left, right)
        
        
    def mergeTwoSortedLists(self, first, second):
        if not first and not second:
            return first
        if not first or not second:
            return first or second
        dummy_node=cur=ListNode(0)
        while first and second:
            if first.val<second.val:
                cur.next=first
                first=first.next
            else:
                cur.next=second
                second=second.next
            cur = cur.next
        cur.next= first or second
        return dummy_node.next
        
        
        # pq= PriorityQueue()
        # for i in range(len(lists)):
        #     if lists[i]:
        #         pq.put((lists[i].val,i, lists[i]))
        # dummy_node=cur = ListNode(0)
        # while not pq.empty():
        #     _, i, cur.next= pq.get()
        #     cur = cur.next
        #     if cur.next:
        #         pq.put((cur.next.val,i,  cur.next))
        # return dummy_node.next
            
