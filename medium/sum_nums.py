def sumNums(n: int) -> int:
    return sum(range(1, n + 1))


def sumNums(n: int) -> int:
    # python的and操作如果最后结果为真，返回最后一个表达式的值，or操作如果结果为真，返回第一个结果为真的表达式的值
    return n and n + sumNums(n - 1)
