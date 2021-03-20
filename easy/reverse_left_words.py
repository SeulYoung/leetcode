def reverseLeftWords(s: str, n: int) -> str:
    return s[n:] + s[:n]


def reverseLeftWords(s: str, n: int) -> str:
    str_list = []
    length = len(s)
    for i in range(n, n + length):
        str_list.append(s[i % length])

    return ''.join(str_list)
