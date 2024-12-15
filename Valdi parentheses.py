class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i in matching.values():
                stack.append(i)
            elif i in matching.keys():
                if stack and stack[-1] == matching[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack