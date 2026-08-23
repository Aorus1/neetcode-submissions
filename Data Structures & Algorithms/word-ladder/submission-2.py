class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # basic check to speed things up
        if endWord not in wordList:
            return 0

        # variables
        n = len(wordList)
        wordlen = len(beginWord)

        # build adjacency map
        neighbors = {}
        for word in wordList:
            for i in range(wordlen):
                temp = word[:i] + "*" + word[i+1:]
                if temp not in neighbors:
                    neighbors[temp] = [word]
                else:
                    neighbors[temp].append(word)
              
        # bfs
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while q:
            word, dist = q.popleft()
            for i in range(wordlen):
                temp = word[:i] + "*" + word[i+1:]
                if temp in neighbors:
                    for neighbor in neighbors[temp]:
                        if neighbor == endWord:
                            return dist+1
                        if neighbor not in visited:
                            q.append((neighbor, dist+1))
                            visited.add(neighbor)
                    neighbors[temp] = []
        return 0

                




        
        



            

        


            

            


        


        