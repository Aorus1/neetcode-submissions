import string
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj_list = {char: [] for char in string.ascii_lowercase}

        def strdiff(str1, str2) -> int:
            minlen = min(len(str1), len(str2))
            for i in range(minlen):
                if str1[i] != str2[i]:
                    return i
            return -1
        all_letters = set()
        for word in words:
            for l in word:
                all_letters.add(l)
        

        letters = set()
        

        for i in range(n-1):
            di = strdiff(words[i], words[i+1])
            if di == -1:
                if len(words[i]) > len(words[i+1]):
                    return ""
                continue
            if words[i][di] == words[i+1][di]:
                letters.add(words[i][di])
                continue
            adj_list[words[i][di]].append(words[i+1][di])
            letters.add(words[i][di])
            letters.add(words[i+1][di])

        indeg = {c: 0 for c in letters}
        for l in letters:
            for neigh in adj_list[l]:
                indeg[neigh] += 1
        deg0 = set([c for c in indeg if indeg[c] == 0])

        L = ""
        while deg0:
            node = deg0.pop()
            L = L + node
            for neigh in adj_list[node]:
                indeg[neigh] -= 1
                if (indeg[neigh] == 0):
                    deg0.add(neigh)

        if any(indeg[c] != 0 for c in letters):
            return ""
        else:
            return L + "".join(str(x) for x in all_letters - letters) 
            

            

        