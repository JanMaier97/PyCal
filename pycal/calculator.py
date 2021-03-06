import math

from stack import Stack
from tokenize import tokenize


class Calculator:
    CONSTANTS  = {"e", "pi"}
    FUNCTIONS  = {"sqrt": math.sqrt, "log": math.log, "exp": math.exp}
    OPERATIONS = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "**": 3}

    def __init__(self, expr, variables={}):
        self._tokens = Stack.from_list(tokenize(expr))
        self._operators = Stack()
        self._arguments = Stack()
        self._variables = variables

    def evaluate(self):
        """Return the result of the function or raise a SyntaxError."""

        while not self._tokens.is_empty():
            next_operator = self._tokens.top()
            self._tokens.pop()

            if next_operator in self.CONSTANTS:
                self._arguments.push(self._get_constant(next_operator))
                continue

            if isinstance(next_operator, int):
                self._arguments.push(next_operator)
                continue

            if (self._operators.is_empty() or next_operator == "("):
                self._operators.push(next_operator)
                continue

            top_operator = self._operators.top()

            if top_operator == "(" and next_operator == ")":
                self._operators.pop()
            elif (next_operator == ")" or
                  self._eval_before(top_operator, next_operator)):
                self._pop_and_evaluate()
                self._tokens.push(next_operator)
            else:
                self._operators.push(next_operator)

        while not self._operators.is_empty():
            self._pop_and_evaluate()

        result = self._arguments.top()
        self._arguments.pop()

        if not self._operators.is_empty() or not self._arguments.is_empty():
            raise SyntaxError("The function could not be computed.")
        return result

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
        """Return the precedence of the given operator as int or raise an
           AssertionError."""

        assert operator in self.FUNCTIONS or operator in self.OPERATIONS, (
               f"Invalid operator {operator}.")

        if operator in self.FUNCTIONS:
            return 4
        else:
            return self.OPERATIONS[operator]

    def _pop_and_evaluate(self):
        rhs = self._arguments.top()
        self._arguments.pop()

        op = self._operators.top()
        self._operators.pop()

        if op in self.FUNCTIONS:
            self._arguments.push(self._compute_function(rhs, op))
            return

        lhs = self._arguments.top()
        self._arguments.pop()

        if op in self.OPERATIONS:
            self._arguments.push(self._compute_operation(lhs, rhs, op))

        raise ValueError("Invalid operator {op}")

    def _get_constant(self, const):
        const = const.lower()
        assert const in self.CONSTANTS, f"Invalid constant {const}."

        if const == "e":
            return math.e
        elif const == "pi":
            return math.pi

    def _compute_operation(self, lhs, rhs, op):
        assert op in self.OPERATIONS, f"Invalid op {op}."

        if op == "+":
            return lhs + rhs
        elif op == "-":
            return lhs - rhs
        elif op == "*":
            return lhs * rhs
        elif op == "/":
            return lhs / rhs
        elif op == "%":
            return lhs % rhs
        elif op == "**":
            return lhs ** rhs

    def _compute_function(self, arg, func):
        """Return the result of the given func with its argument, else raise
           an AssertError."""

        assert func in self.FUNCTIONS, f"Invalid funktion {func}."

        if func in self.FUNCTIONS:
            if func == "sqrt":
                return math.sqrt(arg)
            elif func == "log":
                return math.log(arg)
            elif func == "exp":
                return math.exp(arg)

    def __str__(self):
        """Return the current state as a string for pretty printing."""

        return (self._tokens.__str__() +
                self._arguments.__str__() +
                self._operators.__str__())


if __name__ == "__main__":
    c = Calculator("(1+2)*(3-4)")
    print(c.evaluate())

    c = Calculator("-3 + 1")
    print(c.evaluate())

    c = Calculator("log(2+5)")
    print(c.evaluate())

    c = Calculator("e + pi")
    print(c.evaluate())
