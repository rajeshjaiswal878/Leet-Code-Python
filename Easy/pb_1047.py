import string


def remove_adjecent_brute_force(str):
    res = []
    for ch in str:
        if res and ch == res[-1]:
            res.pop()
        else:
            res.append(ch)
    return ''.join(res)


def remove_duplicates_imprvised(S):
    dub = {2 * ch for ch in string.ascii_lowercase}
    for pair in dub:
        S = S.replace(pair, '')
    return S


result = remove_adjecent_brute_force('abbaca')
result_imp = remove_duplicates_imprvised('abbaca')
print(result_imp)
