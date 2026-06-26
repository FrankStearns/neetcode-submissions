class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        valid = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for parenthesis in s:
            if parenthesis in valid:
                check.append(valid[parenthesis])
            else:
                if len(check) < 1:
                    return False
                if parenthesis != check.pop():
                    return False
        if len(check) != 0:
            return False
        return True
                    