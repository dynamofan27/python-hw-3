import sys

a = sys.argv[1]
b = sys.argv[3]
op = sys.argv[2]


def calc(left_operand, right_operand, operation):
    if not left_operand.isnumeric() or not right_operand.isnumeric():
        exit("Error, left or righ opearnds should be Integers!")
    else:
        left_operand = int(left_operand)
        right_operand = int(right_operand)

    if len(sys.argv) > 4:
        print("Error. Too much variables.")
    elif operation not in ["+", "-", "/", "*"]:
        print("Error. Supported operations: +, -, *, /. If you are using * op, please try to run the script is python "
              "calculate.py 2 '*' 3")
    elif operation == "/" and right_operand == 0:
        print("Error, division by zero - restricted.")
    elif operation == "+":
        print(left_operand + right_operand)
    elif operation == "-":
        print(left_operand - right_operand)
    elif operation == "*":
        print(left_operand * right_operand)
    elif operation == "/":
        if left_operand % right_operand == 0:
            print(left_operand // right_operand)
        else:
            print(left_operand / right_operand)
    elif operation == "%":
        print(left_operand % right_operand)
    else:
        print("Error, something went wrong. Please, try again.")


calc(a, b, op)
