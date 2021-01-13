class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if str_x[0] == '-':
            x = - int(str_x[:0:-1])
        else:
            x = int(str_x[::-1])
        return x if -2147483648 < x < 2147483647 else 0

    def reverse(self, x: int) -> int:
        abs_x, rev = abs(x), 0
        # boundary = 2147483647 if x > 0 else 2147483648
        boundary = (1 << 31) - 1 if x > 0 else 1 << 31
        
        while abs_x != 0:
            rev = rev * 10 + abs_x % 10
            if rev > boundary:
                return 0
            abs_x //= 10
        return rev if x > 0 else -rev
