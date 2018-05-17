from stack import Stack


class Calculator:
    def __init__(self, expr):
        self.tokens = Stack.from_list(expr)
        self.operators = Stack()
        self.arguments = Stack()

    def evaluate(self):
        while not self.tokens.is_empty():
            if is_int(self.tokens.top()):
                self.arguments.push(self.tokens.top())
                self.tokens.pop()
                continue

            next_operator = self.tokens.top()
            self.tokens.pop()

            if (self.operators.is_empty() or self.operators.top() == "("):
                self.operators.push(next_operator)
                continue

            top_operator = self.operators.top()

            if top_operator == "(" and next_operator == ")":
                self.operators.pop()
            elif next_operator == ")" or self._eval_before(top_operator, next_operator):
                pass
            else:
                self.operators.push(next_operator)

            while not self.operators.is_empty():
                pass

            return self.arguments.top()

    def _eval_before(stack_op, next_op):
        precedence_map = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "**": 3}
        if stack_op == "(":
            return False


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
