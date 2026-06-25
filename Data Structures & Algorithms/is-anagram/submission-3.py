class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDict = {}
        for letter in s:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
        for letter in t:
            if letter not in letterDict:
                return False
            if letter in letterDict:
                letterDict[letter] -= 1
                if letterDict[letter] < 0:
                    return False
        for key in letterDict:
            if letterDict[key] > 0:
                return False
        return True
