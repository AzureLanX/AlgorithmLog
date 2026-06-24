class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
            stack.append(i)
        
        return not stack
