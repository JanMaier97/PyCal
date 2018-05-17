import sys
import math

from stack import Stack
from tokenize import tokenize


class Calculator:
    CONSTANTS = {"e", "pi"}
    FUNCTIONS = {"sqrt", "log", "exp"}
    OPERATIONS = {"+", "-", "*", "/", "%"}

    def __init__(self, expr, variables={}):
        self.tokens = Stack.from_list(tokenize(expr))
        self.operators = Stack()
        self.arguments = Stack()
        self.variables = variables

    def evaluate(self):
        while not self.tokens.is_empty():
            self.print_()
            input()

            next_operator = self.tokens.top()
            self.tokens.pop()

            if next_operator in self.CONSTANTS:
                self.arguments.push(self._get_constant(next_operator))
                continue

            if next_operator.isdigit():
                self.arguments.push(next_operator)
                continue

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
                return stack_op in {"+", "-", "*", "/", "%"}
            return True
        return False

    def _get_precedence(self, operator):
        precedence = {
                "+": 1,
                "-": 1,
                "*": 2,
                "/": 2,
                "%": 2,
                "**": 3,
                "exp": 4,
                "log": 4,
                "sqrt": 4,
                }
        assert operator in precedence, f"Invalid operator {operator}."
        return precedence[operator]

    def _pop_and_evaluate(self):
        rhs = int(self.arguments.top())
        self.arguments.pop()

        op = self.operators.top()
        self.operators.pop()

        if op in self.FUNCTIONS:
            if op == "sqrt":
                result = math.sqrt(rhs)
            elif op == "log":
                result = math.log(rhs)
            elif op == "exp":
                result = math.exp(rhs)
            self.arguments.push(result)
            return

        lhs = int(self.arguments.top())
        self.arguments.pop()

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

    def _get_constant(self, const):
        const = const.lower()
        assert const in self.CONSTANTS, f"Invalid constant {const}."
        if const == "e":
            return math.e
        elif const == "pi":
            return math.pi

    def print_(self):
        print(self.tokens)
        print(self.arguments)
        print(self.operators)


if __name__ == "__main__":
    # c = Calculator("(1+2)*(3-4)")
    # print(c.evaluate())

    # c = Calculator("-3 + 1")
    # print(c.evaluate())

    # c = Calculator("log(2+5)")
    # print(c.evaluate())

    c = Calculator("e + pi")
    print(c.evaluate())
