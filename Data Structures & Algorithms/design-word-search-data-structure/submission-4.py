class Node:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True

        

    def search(self, word: str) -> bool:
        # if word != "b..":
        #     return False
        cur = self.root
        def dfs(cur, i):
            print(cur, i, word[i:])
            if len(word[i:]) == 0 and cur.end:
                return True
            for c in word[i:]:
                if c in cur.children:
                    return dfs(cur.children[c], i+1)
                if c == ".":
                    for ch in cur.children:
                        if dfs(cur.children[ch], i+1):
                            return True
                return False

            return False
        return dfs(cur, 0);
            