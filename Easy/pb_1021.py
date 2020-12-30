def remove_outer_parenthesis(str):
    result, opened = [], 0
    for ch in str:
        if ch == '(' and opened > 0:
            result.append(ch)
        if ch == ')' and opened > 1:
            result.append(ch)
        opened += 1 if ch == '(' else -1
    return ''.join(result)


res = remove_outer_parenthesis('(())')
print(res)
