class MinStack:

    def __init__(self):
        self.q = []
        self.minstack = []
        return None

    def push(self, val: int) -> None:
        self.q.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)

        return None

    def pop(self) -> None:
        if self.q[-1] == self.minstack[-1]:
            self.minstack.pop()

        self.q.pop()
        return None

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
        
