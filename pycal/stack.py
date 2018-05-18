import copy


class Stack:
    ERROR_EMPTY_STACK = "Error, stack is empty"

    def __init__(self):
        """Initialize the empty stack."""
        self._elements = []

    def pop(self):
        """Remove the top element of the stack or throw an AssertionError."""
        assert self.is_empty() is False, self.ERROR_EMPTY_STACK
        self._elements.pop()

    def top(self):
        """Return the top element of the stack or throw an AssertionError."""
        assert self.is_empty() is False, self.ERROR_EMPTY_STACK
        return self._elements[-1]

    def push(self, item):
        """Add an item to the top of the stack."""
        self._elements.append(item)

    def is_empty(self):
        """Return True if the stack is empty, else return False."""
        return self._elements == []

    @staticmethod
    def from_list(elements):
        """Return a stack containing the elements of the given list."""
        stack = Stack()
        for item in elements[::-1]:
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
