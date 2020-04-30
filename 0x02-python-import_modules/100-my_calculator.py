#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if sys.argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if sys.argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if sys.argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
