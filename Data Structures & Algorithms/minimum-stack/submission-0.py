class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.n = -1
        self.m = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.n += 1
        if self.m == -1 or val <= self.getMin():
            self.min_stack.append(val)
            self.m += 1


    def pop(self) -> None:
        if self.n > -1:
            if self.getMin() == self.stack.pop():
                del self.min_stack[-1]
                self.m -= 1
            self.n -= 1
        

    def top(self) -> int:
        return self.stack[self.n] 
        

    def getMin(self) -> int:
        return self.min_stack[self.m]
        
