class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # basic check to speed things up
        if endWord not in wordList:
            return 0

        # variables
        n = len(wordList)
        wordlen = len(beginWord)
        def valid(a, b):
            diff = 0
            for i in range(wordlen):
                if a[i] != b[i]:
                    diff += 1
                
            return diff == 1
        neighbors = {}

        for word in [beginWord] + wordList:
            for i in range(wordlen):
                temp = word[:i] + "*" + word[i+1:]
                if temp not in neighbors:
                    neighbors[temp] = [word]
                else:
                    neighbors[temp].append(word)
                if word not in neighbors:
                    neighbors[word] = [temp]
                else:
                    neighbors[word].append(temp)
                
            



        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while q:
            val, dist = q.popleft()
            if "*" in val:
                dist -= 1

            for neighbor in neighbors[val]:
                if neighbor == endWord:
                    return dist + 1
                if neighbor not in visited:
                    q.append((neighbor, dist+1))
                    visited.add(neighbor)
        return 0
                




        
        



            

        


            

            


        


        