class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        anaDict = {}
        for word in strs:
            sword = "".join(sorted(word))
            if sword in anaDict:
                anaDict[sword].append(word)
            else:
                anaDict[sword] = [word]
        out = []
        for key in anaDict:
            out.append(anaDict[key])
        return out
