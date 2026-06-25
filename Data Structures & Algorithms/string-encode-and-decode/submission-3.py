class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + "#"
            out += word
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        pointer = 0
        i = 1
        while pointer < len(s):
            while s[pointer+i] != "#":
                i+=1
            length = int(s[pointer:pointer+i])
            out.append(s[pointer + 1+i:pointer+length+1+i])
            pointer = pointer+length+1+i
            i = 1
        return out
