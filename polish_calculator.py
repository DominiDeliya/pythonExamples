#small program that computes arithmetic expressions in postfix notation,
#also known as reverse polish notation or RPN.
#used lambda and math function

import math
operators = {
    "+": (lambda a, b: a+b),
    "-": (lambda a, b: a-b),
    "/": (lambda a, b: a/b),
    "*": (lambda a, b: a*b),
    "sqrt": (lambda a : math.sqrt(a))
}

def calc(expression):

     tokens = expression.split()
     stack  = []

     for token in tokens:
         print(stack)
         if token in operators:

             if token != "sqrt":
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = operators[token](arg2,arg1)
                stack.append(result)
             else:
                arg1 = stack.pop()
                result = operators[token](arg1)
                stack.append(result)
         else:
             stack.append(int(token))

     return stack.pop()

print(calc("5 4 2 * 3 + + sqrt"))


