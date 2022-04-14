class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return false
        open_bracket = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in open_bracket.values():
                stack.append(i)
            else:
