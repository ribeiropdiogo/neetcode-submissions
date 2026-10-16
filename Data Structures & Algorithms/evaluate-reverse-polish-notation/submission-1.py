class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expr = 0

        for i in range(0,len(tokens)):
            if tokens[i] not in ['+','-','/','*']:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    expr = a + b
                elif tokens[i] == '-':
                    expr = a - b
                elif tokens[i] == '/':
                    expr = int(a / b)
                elif tokens[i] == '*':
                    expr = a * b
                stack.append(expr)


        return stack.pop()

        