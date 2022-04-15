class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return false
        open_bracket = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in open_bracket.values():
                stack.append(i)
            elif len(stack) == 0 and i in open_bracket.keys():
                return False
            elif open_bracket[i] == stack[len(stack)-1] and len(stack)>0:
                stack.pop()
            elif open_bracket[i] != stack[len(stack) - 1] and len(stack)>0:
                return False
            
        if len(stack)==0:
            return True
