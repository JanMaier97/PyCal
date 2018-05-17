import re


def tokenize(string):
    """Return a list of tokens of a mathematical expression."""
    pattern = r"(\b\w*[\.]?\w+\b|[*][*]|[()+*%\/\-])"
    return re.findall(pattern, string)


# simple testing
if __name__ == "__main__":
    expression = "10 * (20 + 100) / sin(x + 8 ** 2)"
    print(tokenize(expression))
