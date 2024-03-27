"""
we can have a list with normal pop and append since 
for a stack, that would remain constant time.

for getting the min value, we track the curr min of each substack.

that can be done by using an array, and each index is related to the subsize of the stack.
then, for each substack, we have a related min value. When popping and pushing, we can either delete, or update the curr
min at that position 


"""


def __init__(self):
    self.stack = []
    self.mins = []


def push(self, val: int) -> None:
    if len(self.stack) == 0:
        self.stack.append(val)
        self.mins.append(val)
    else:
        self.stack.append(val)
        self.mins.append(min(self.mins[len(self.stack) - 2], val))


def pop(self) -> None:
    if len(self.stack) == 0:
        return

    self.stack.pop()
    self.mins.pop()


def top(self) -> int:
    return self.stack[-1]


def getMin(self) -> int:
    return self.mins[-1]
