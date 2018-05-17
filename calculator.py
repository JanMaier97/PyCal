import sys

from stack import Stack


class Calculator:
    def __init__(self, expr):
        self.tokens = Stack.from_list(expr)
        self.operators = Stack()
        self.arguments = Stack()

    def evaluate(self):
        while not self.tokens.is_empty():
            self.print_()
            input()
            if self.tokens.top().isdigit():
                self.arguments.push(self.tokens.top())
                self.tokens.pop()
                continue

            next_operator = self.tokens.top()
            self.tokens.pop()

            if (self.operators.is_empty() or next_operator == "("):
                self.operators.push(next_operator)
                continue

            top_operator = self.operators.top()

            if top_operator == "(" and next_operator == ")":
                self.operators.pop()
            elif (next_operator == ")" or
                  self._eval_before(top_operator, next_operator)):
                self._pop_and_evaluate()
                self.tokens.push(next_operator)
            else:
                self.operators.push(next_operator)

        while not self.operators.is_empty():
            self._pop_and_evaluate()

        return self.arguments.top()

    def _eval_before(self, stack_op, next_op):
        if stack_op == "(":
            return False

        stack_prec = self._get_precedence(stack_op)
        next_prec = self._get_precedence(next_op)

        if stack_prec > next_prec:
            return True
        elif stack_prec == next_prec:
            if stack_op == next_op:
                return stack_op in ["+", "-", "*", "/", "%"]
            return True
        return False

    def _get_precedence(self, operator):
        precedence = {
                "+": 1,
                "-": 1,
                "*": 2,
                "/": 2,
                "%": 2,
                "**": 3}
        assert operator in precedence, f"Invalid operator {operator}."
        return precedence[operator]

    def _pop_and_evaluate(self):
        rhs = int(self.arguments.top())
        self.arguments.pop()

        lhs = int(self.arguments.top())
        self.arguments.pop()

        op = self.operators.top()
        self.operators.pop()

        result = 0
        if op == "+":
            result = lhs + rhs
        elif op == "-":
            result = lhs - rhs
        elif op == "*":
            result = lhs * rhs
        elif op == "/":
            result = lhs / rhs
        elif op == "%":
            result = lhs % rhs
        elif op == "**":
            result = lhs % rhs
        else:
            sys.exit(f"Invalid operator {op}")

        self.arguments.push(result)

    def print_(self):
        print(self.tokens)
        print(self.arguments)
        print(self.operators)


if __name__ == "__main__":
    c = Calculator("(1+2)*(3-4)")
    print(c.evaluate())
