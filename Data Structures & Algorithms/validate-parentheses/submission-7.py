class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            st = ord(ss)
            if stack and (ord(stack[-1]) == st - 1 or ord(stack[-1]) == st - 2):
                stack.pop()
            else:
                stack.append(ss)
        return len(stack) == 0