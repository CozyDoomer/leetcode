import re


def calculate(s: str) -> int:
    num = 0
    num_stack = []
    sign_stack = []
    cur_sign = "+"
    sign = 1
    for char in s+"+":
        if char.isdigit():
            num = num + int(char)
        elif char in ["+", "-", "/", "*"]:
            if cur_sign in ["+", "-"]:
                num_stack.append(num)
                sign_stack.append(sign)
                num = 0
                cur_sign = char
            elif cur_sign == "*":
                num_stack[-1] = num_stack[-1]*num
                num = 0
                cur_sign = char
            else:
                num_stack[-1] = num_stack[-1]//num
                num = 0
                cur_sign = char
            if char == "+":
                sign = 1
            elif char == "-":
                sign = -1
    return sum(x*y for x, y in zip(num_stack, sign_stack))


print(calculate("3+2*2"))
