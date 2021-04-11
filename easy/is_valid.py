from collections import deque


#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s):
        stack = deque()
        brackets = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != brackets[c]:
                return False
        # return False if stack else True
        return len(stack) == 0
