# Algorithm used, just use xor, as XOR of two similar things become 0

# Time O(n) space O(1)


def missing_number(arr):

    res = len(arr)
    for i in range(len(arr)):
        res ^= i
        res ^= arr[i]

    return res


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number([0]))
