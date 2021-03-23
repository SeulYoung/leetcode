def hammingWeight(n: int) -> int:
    return bin(n).count('1')


def hammingWeight(n: int) -> int:
    return sum(1 for i in range(32) if n & (1 << i))


def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
