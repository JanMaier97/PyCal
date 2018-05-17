import copy


class Stack:
    ERROR_EMPTY_STACK = "Error, stack is empty"

    def __init__(self):
        """Initialize the empty stack."""
        self.elements = []

    def pop(self):
        """Remove the top element of the stack or throw an AssertionError."""
        assert self.is_empty() is False, self.ERROR_EMPTY_STACK
        self.elements = self.elements[:-1]

    def top(self):
        """Return the top element of the stack or throw an AssertionError."""
        assert self.is_empty() is False, self.ERROR_EMPTY_STACK
        return self.elements[-1]

    def push(self, item):
        """Add an item to the top of the stack."""
        self.elements.append(item)

    def is_empty(self):
        """Return True if the stack is empty, else return False."""
        return self.elements == []

    @staticmethod
    def from_list(elements):
        """Return a stack containing the elements of the given list."""
        stack = Stack()
        for item in elements:
            stack.push(item)
        return stack

    def __str__(self):
        """Return the string representation of the stack."""
        value_str = self._stack_to_string(copy.deepcopy(self))
        line = "-" * len(value_str)
        return "\n".join([line, value_str, line])

    def _stack_to_string(self, stack):
        """Return a string of the stack values seperated by "|"."""
        value_str = " |"
        while not stack.is_empty():
            value_str = F"| {stack.top()} {value_str}"
            stack.pop()

        return value_str


# simple testing
if __name__ == "__main__":
    print("Testing")

    MAX_COUNT = 10

    test_stack = Stack()
    for i in range(MAX_COUNT):
        test_stack.push(i + 1)
        print(test_stack)

    while not test_stack.is_empty():
        test_stack.pop()
        print(test_stack)
