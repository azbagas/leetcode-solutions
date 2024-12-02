class MinStack:

    def __init__(self):
        '''
        Element of stack: [val, min]
        val: the real value
        min: minimum number in the stack for the current val
        '''
        self.stack: list[list[int]] = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
            return
        
        current_min = self.stack[-1][-1] 
        if val < current_min:
            # The new val is the minimum number
            self.stack.append([val, val])
        else:
            # The minimum number is still the same
            self.stack.append([val, current_min]) 

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()