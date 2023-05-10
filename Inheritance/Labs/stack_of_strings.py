class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self) -> str:
        last_element = self.data.pop()
        return last_element

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return f"[{', '.join([self.data[el] for el in range(len(self.data) - 1, -1, -1)])}]"


# stack = Stack()
# stack.push('Apple')
# stack.push('Banana')
# stack.push('Orange')
# print(stack.pop())
# print(stack.top())
# print(stack.is_empty())
# print(stack)




