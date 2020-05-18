#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
    except (ValueError, TypeError) as error:
        print("{}".format(sys.error), file=sys.stderr)
        return False
    return True
