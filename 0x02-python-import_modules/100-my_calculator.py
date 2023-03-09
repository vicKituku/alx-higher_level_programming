#!/usr/bin/python3
# Author: Victor Mwangangi
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, operators[argv[2]](a, b)))
