class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal,val)
        

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.minVal:
            self.minVal = float("inf")
            for v in self.stack:
                if v < self.minVal:
                    self.minVal = v

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
        
