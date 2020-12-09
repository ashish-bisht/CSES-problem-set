def creating_strings(string):
    res = []
    string = list(string)
    string.sort()
    helper(string, len(string), [], res)
    print(len(res))
    return res


def helper(string, string_len, cur, res):

    if len(cur) == string_len:
        res.append("".join(cur))

        return

    for i in range(len(string)):
        if i > 0 and string[i-1] == string[i]:  # handling duplicates
            continue

        helper(string[:i]+string[i+1:], string_len, cur + [string[i]], res)


print(creating_strings("aabac"))
