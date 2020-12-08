# This is a maximum-length substring containing only one type of character.

# Time O(n) space O(1)

def repetition(string):
    if not string:
        return 0
    ans = 1
    left = 1
    while left < len(string):
        cur_max = 1
        if string[left] == string[left-1]:
            while left < len(string) and string[left] == string[left-1]:
                left += 1
                cur_max += 1
        ans = max(ans, cur_max)
        left += 1
    return ans


print(repetition("ATTCGGGA"))  # 3
print(repetition("ATTCGGGAAAA"))  # 4
print(repetition("A"))  # 1
print(repetition(""))  # 1
