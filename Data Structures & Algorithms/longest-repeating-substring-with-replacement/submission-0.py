class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        freq = {}
        n = len(s)
        l = 0
        maxchar = 0
        for r in range(n):
            char = s[r]
            if char not in freq:
                freq[char] = 1
            else: 
                freq[char] += 1
            if freq[char] > maxchar:
                maxchar = freq[char]
            if maxchar + k < r-l+1:
                while maxchar + k < r-l+1:
                    freq[s[l]] -= 1
                    l += 1
            out = max(out,r-l+1)
        return out
            