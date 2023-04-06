class ExampleStack:
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)

    def pop(self):
        if not self.empty():
            return self.st.pop()
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.st[-1]
        else:
            return None

    def search(self, item):
        try:
            return len(self.st) - self.st[::-1].index(item)
        except ValueError:
            return -1

    def empty(self):
        return len(self.st) == 0


example_stack = ExampleStack()

example_stack.push("Aku")
example_stack.push("Anak")
example_stack.push("Indonesia")

print("Next : " + example_stack.peek())
example_stack.push("Raya")
print(example_stack.pop())
example_stack.push("!")

count = example_stack.search("Aku")
while count != -1 and count > 1:
    example_stack.pop()
    count -= 1

print(example_stack.pop())
print(example_stack.empty())
