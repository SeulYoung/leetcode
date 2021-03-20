from typing import List


def evalRPN(tokens: List[str]) -> int:
    num_stack = []
    for s in tokens:
        try:
            num_stack.append(int(s))
        except ValueError:
            n, m = num_stack.pop(), num_stack.pop()
            # 面试中不应使用该函数
            num_stack.append(int(eval(f'{m}{s}{n}')))

    return num_stack.pop()


def evalRPN(tokens: List[str]) -> int:
    str_to_op = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }

    num_stack = []
    for s in tokens:
        try:
            num = int(s)
        except ValueError:
            n, m = num_stack.pop(), num_stack.pop()
            num = str_to_op[s](m, n)
        finally:
            num_stack.append(num)

    return num_stack.pop()
