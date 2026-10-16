class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            stack = []
            closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
            for i, c in enumerate(s):
                if len(stack) == 0:
                    stack.append(c)
                else:
                    top = stack[-1]
                    if c in closeToOpen and closeToOpen[c] == top:
                        stack.pop()
                    else:
                        stack.append(c)
            if len(stack) > 0:
                return False
        else:
            return False
        return True
        