from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s)==Counter(t) if len(s)==len(t) else False
        #solution 3 use map
        # first, second= {},{}
        # if len(s)!= len(t):
        #     return False
        # for i in s:
        #     first[i] = first.get(i,0)+1
        # for i in t:
        #     second[i]= second.get(i,0)+1
        # return first==second
        
        #Solution 2 use my own vector
        # first, second = [0]*26, [0]*26
        # if len(s)!= len(t):
        #     return False
        # for i in range(len(s)):
        #     first[ord(s[i])- ord('a')]+=1
        #     second[ord(t[i])- ord('a')]+=1
        # return first==second
        
        #Solution 1 use sorted() O(n)=  n* log(n)
        return sorted(s)==sorted(t)
        
