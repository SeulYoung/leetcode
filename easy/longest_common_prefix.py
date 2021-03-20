from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    prefix, count = strs[0], len(strs)
    for i in range(1, count):
        idx = 0
        length = min(len(prefix), len(strs[i]))
        while idx < length and prefix[idx] == strs[i][idx]:
            idx += 1
        prefix = strs[i][:idx]

        if not prefix:
            break

    return prefix


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    count = len(strs)
    for i in range(len(strs[0])):
        c = strs[0][i]
        # for j in range(count):
        #     if i == len(strs[j]) or c != strs[j][i]:
        #         return strs[0][:i]
        if any(i == len(strs[j]) or c != strs[j][i] for j in range(count)):
            return strs[0][:i]

    return strs[0]


def longestCommonPrefix(strs: List[str]) -> str:
    def is_common_prefix(length):
        common_str, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == common_str for i in range(1, count))

    if not strs:
        return ''

    low, high = 0, min(len(s) for s in strs)
    while low < high:
        # 不加1虽然结果正确，但是会导致超时
        mid = (high - low + 1) // 2 + low
        if is_common_prefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]
