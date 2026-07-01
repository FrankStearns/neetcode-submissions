class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        letters = []
        index = []
        tset = set(t)
        for i in range(len(s)):
            if s[i] in tset:
                letters.append(s[i])
                index.append(i)
        tCount = Counter(t)
        l = 0
        good = 0
        best = ""
        for r in range(len(letters)):
            tCount[letters[r]] -= 1
            if tCount[letters[r]] == 0:
                good += 1
            if good == len(tCount):
                while good == len(tCount):
                    tCount[letters[l]] += 1
                    if tCount[letters[l]] > 0:
                        good -= 1
                    l += 1
                new = s[index[l-1]:index[r]+1]
                if len(new) < len(best) or len(best) == 0:
                    best = s[index[l-1]:index[r]+1]
        return best
                    

