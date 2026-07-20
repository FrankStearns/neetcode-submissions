class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        anagrams = {}
        for word in strs:
            letters = "".join(sorted(word))
            if letters not in anagrams:
                anagrams[letters] = [word]
            else:
                anagrams[letters].append(word)
        out = []
        for key in anagrams:
            out.append(anagrams[key])
        return out

