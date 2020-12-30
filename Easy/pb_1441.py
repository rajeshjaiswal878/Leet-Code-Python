def build_array(arr, n):
    result = []
    s = set(arr)
    for i in range(1, arr[-1] + 1):
        result.append('Push')
        if i not in s:
            result.append('Pop')
    return result


def build_array_imp(arr, n):
    result = []
    for i in range(1, arr[-1] + 1):
        if i in arr:
            result.append('Push')
        else:
            result.append('Push')
            result.append('Pop')
    return result


res = build_array_imp([1, 2], 4)
print(res)
