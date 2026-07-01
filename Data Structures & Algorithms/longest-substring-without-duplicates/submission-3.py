class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        out = 1
        l = 0
        dups = set()
        for r in range(len(s)):
            if s[r] not in dups:
                dups.add(s[r])
            else:
                while s[r] in dups:
                    dups.remove(s[l])
                    l += 1
                dups.add(s[r])
            out = max(r-l + 1, out)
        return out

            
            