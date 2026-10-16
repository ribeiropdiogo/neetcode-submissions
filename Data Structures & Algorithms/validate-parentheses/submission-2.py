class Solution:
    def close(self,a: str, b: str) -> bool:
        possible = [('[',']'),('(',')'),('{','}')]
        pair = (a,b).sort()
        if pair in possible:
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            stack = []
            for i, c in enumerate(s):
                if len(stack) == 0:
                    stack.append(c)
                else:
                    top = stack[-1]
                    if top == '(' and c == ')':
                        stack.pop()
                    elif top == '[' and c == ']':
                        stack.pop()
                    elif top == '{' and c == '}':
                        stack.pop()
                    else:
                        stack.append(c)
            if len(stack) > 0:
                return False
        else:
            return False
        return True
        