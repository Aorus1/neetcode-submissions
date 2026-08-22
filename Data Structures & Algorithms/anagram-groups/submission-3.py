class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sorted string as key, values be different strings
        anagrams = {}
        for string in strs:
            sorted_version = "".join(sorted(string))
            if sorted_version in anagrams:
                anagrams[sorted_version].append(string)
            else:
                anagrams[sorted_version] = [string]
        return(list(anagrams.values()))
        