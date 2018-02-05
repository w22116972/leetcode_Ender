"""
Reverse Polish Notation == Postfix notation
"""


# def eval(x, y, operator):
#     if operator == '/' and y == 0:
#         return 0
#     hash_operator = {
#         '+': x + y,
#         '-': x - y,
#         '*': x * y,
#         '/': int(float(x) / y),
#     }
#     return hash_operator[operator]


def is_operator(token):
    if token in ['+', '-', '*', '/']:
        return True
    return False

def eval_RPN(s):
    stack = []
    for token in s:
        if is_operator(token):
            stack.append(int(eval(str(float(stack.pop(-2))) + s + str(stack.pop(-1)))))
        else:
            stack.append(float(token))
    return int(stack.pop())

assert eval_RPN(["8", "1", "2", "+", "2", "*", "-"]) == 2
print(eval_RPN(["1", "0", "/"]))
print(eval_RPN(["6", "-132", "/"]))