class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        #wordList.add(beginWord)
        #wordList.add(endWord)
        dic = self.construct_dict(wordList)
        return self.bfs_words(beginWord, endWord, dic)
    def construct_dict(self, wordList):
        d = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i]+"_"+word[i+1:]
                d[s] = d[s]+[word]
        return d
    def bfs_words(self, begin, end, dic_words):
        queue, visited = collections.deque([(begin, 1)]), set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word==end:
                    return steps
                for i in range(len(word)):
                    s = word[:i]+"_"+word[i+1:]
                    neigh_words = dic_words[s]
                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, steps+1))
        return 0
