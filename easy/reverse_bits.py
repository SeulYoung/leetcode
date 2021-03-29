def reverseBits(n: int) -> int:
    bin_n = list(bin(n)[2:])
    bin_n.reverse()
    bin_n.extend(['0'] * (32 - len(bin_n)))
    return int(''.join(bin_n), 2)


def reverseBits(n: int) -> int:
    rtn = 0
    for i in range(32):
        rtn = (rtn << 1) | (n & 1)
        n >>= 1
    return rtn


def reverseBits(n: int) -> int:
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n
