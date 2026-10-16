class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val-self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        enc = self.stack.pop()
        if enc < 0:
            self.min = self.min - enc

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min

        
