class MinStack:

    def __init__(self):
        self.elems = []
        self.min_id = []
        self.mini = float("inf") 

    def push(self, val: int) -> None:
        self.elems = self.elems + [val]
        old_min = self.mini
        self.mini = min(self.mini, val)
        if len(self.min_id) == 0:
            self.min_id.append(len(self.elems)-1)
        elif old_min == self.mini:
            self.min_id.append(self.min_id[-1])
        else:
            self.min_id.append(len(self.elems)-1)
    def pop(self) -> None:
        self.elems.pop()
        self.min_id.pop()
        self.mini = self.elems[self.min_id[-1]] if self.min_id else float("inf")

    def top(self) -> int:
        return self.elems[-1]

    def getMin(self) -> int:
        return self.mini
