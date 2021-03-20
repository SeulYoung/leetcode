from typing import List


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    count = 0
    # if ruleKey == 'type':
    #     ruleKey = 0
    # elif ruleKey == 'color':
    #     ruleKey = 1
    # else:
    #     ruleKey = 2
    key_map = {'type': 0, 'color': 1, 'name': 2}
    for item in items:
        if item[key_map[ruleKey]] == ruleValue:
            count += 1
    return count


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    key_map = {'type': 0, 'color': 1, 'name': 2}
    return sum(item[key_map[ruleKey]] == ruleValue for item in items)
