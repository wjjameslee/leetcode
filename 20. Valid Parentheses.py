class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if (c == ')' or c == '}' or c == ']') and len(stack) == 0:
                return False
            if c == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            if c == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            if c == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False
                