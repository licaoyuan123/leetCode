from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic =collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dic:
            
            val =self.dic.pop(key)
            self.dic[key] =val
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
        else:
            if self.capacity>0:
                self.capacity-=1
            else:
                self.dic.popitem(last=False)
                self.dic[key] = value
        self.dic[key] = value
        


class Node(object):
    def __init__(self, k:int, v:int):
        self.key=k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic ={}
        self.head = Node(0, 0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add(self, node):
        first =self.head.next
        self.head.next = node
        node.next = first
        first.prev = node
        node.prev = self.head
        
    def _del(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt

        
    def get(self, key: int) -> int:
        if key in self.dic:
            n =self.dic[key]
            self._del(n)
            self._add(n)
            return n.val
            #return self.dic[key]
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.dic:
            self._del(self.dic[key])
        
        node =Node(key, val)
        self._add(node)
        self.dic[key] = node
        if len(self.dic)>self.capacity:
            last = self.tail.prev
            self._del(last)
            del self.dic[last.key]
#Below method can not identify whether updating a value or inserting a new value
#         if self.capacity>0:
#             self.capacity-=1
#             self._add(node)
#             self.dic[key] = node
#         else:
#             self.dic[key] = node
#             self._add(node)
            
#             last = self.tail.prev
#             # key_to_del = 
#             #del self.dic[last.key]
#             self._del(last)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
