class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char not in match:
                stack.append(char)
            else:
                if not stack or match[char] != stack[-1]:
                    return False
                stack.pop()

        return not stack
        
        