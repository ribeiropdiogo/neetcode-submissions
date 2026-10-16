class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            stack = []
            closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
            for i, c in enumerate(s):
                if c in closeToOpen:
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            if len(stack) > 0:
                return False
        else:
            return False
        return True
        