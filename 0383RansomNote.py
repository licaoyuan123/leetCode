import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter1 = collections.Counter(ransomNote)
        counter2 = collections.Counter(magazine)
        for i in counter1:
            if counter1[i] >counter2[i]:
                return False
        return True
        #return all(ransomNote.count(i)<=magazine.count(i) for i in set(ransomNote) )
