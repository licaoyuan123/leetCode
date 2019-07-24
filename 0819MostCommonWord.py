class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banset = set(banned)
        paragraph = paragraph.replace(",", " ")
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
        
        
#         paragraph = paragraph.replace(",", " ")
#         # paragraph = paragraph.replace(".", " ")
#         # paragraph = paragraph.replace("!", " ")
#         # paragraph = paragraph.replace("'", " ")
#         # paragraph = paragraph.replace("?", " ")
#         # paragraph = paragraph.replace(";", " ")
        
#         for c in "!?\',;.":
#             paragraph.replace(c, " ")
#         banned = set(banned)
#         #paragraph.replace(",", " ")
#         count = collections.Counter(word for word in paragraph.lower().split(" ") )
#         ans, best="", 0
#         for word in count:
#             if count[word]>best and word not in banned:
#                 ans = word
#                 best= count[word]
#         return ans
        
