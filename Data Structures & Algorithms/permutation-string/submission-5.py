class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        count = Counter(s2[0:len(s1)])
        print(count)
        if count == s1_count:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            count[s2[r]] += 1
            count[s2[l]] -= 1
            l += 1
            print(count)
            if count == s1_count:
                return True
        return False