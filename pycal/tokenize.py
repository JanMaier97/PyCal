import re


def tokenize(s):
    """Transform the string s into a list of tokens.  The string s
       is supposed to represent a mathematical expression.
    """
    lexSpec = r""" ([ \t]+)               |  # blanks and tabs
                   (0|-?[1-9][0-9]*)      |  # integer
                   ([A-Za-z][A-Za-z0-9]*) |  # identifier
                   (\*\*)                 |  # power
                   ([()+\-*/%])              # operator
               """
    scanner   = re.compile(lexSpec, re.VERBOSE)
    tokenList = re.findall(scanner, s)
    isNumber  = re.compile("0|[1-9][0-9]*")
    isSpace   = re.compile("[ \t]+")
    result    = []
    for ws, number, identifier, power, operator in tokenList:
        if ws:        # skip blanks and tabs
            continue
        if number:
            result += [int(number)]
            continue
        if identifier:
            result += [identifier]
            continue
        if power:
            result += [power]
            continue
        if operator:
            result += [operator]
    return result
