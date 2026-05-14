class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack: list[str] = ["f"]
        for char in s:
            if char == '(':
                stack.append(char)
                continue
            if char == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
                continue
            if char == '{':
                stack.append(char)
                continue
            if char == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
                continue
            if char == '[':
                stack.append(char)
                continue
            if char == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
                continue
        return len(stack) == 1