from collections import Counter
import heapq


def palindrome_order(string):

    char_counter = Counter(string)
    single_char_count = 0
    heap = []
    for key, val in char_counter.items():
        if val % 2 != 0:
            single_char_count += 1
        if single_char_count > 1:
            return False
        heapq.heappush(heap, [-val, key])

    first_half = []
    second_half = []

    while len(heap) > 1:
        val, key = heapq.heappop(heap)
        val = - val//2
        first_half.append(val*key)
        second_half.append(val*key)
    _, last_char = heapq.heappop(heap)
    first_half.append(last_char)
    res = first_half + second_half[::-1]

    return "".join(res)


print(palindrome_order("AAAACACBA"))
print(palindrome_order("AAAACACBAZ"))
print(palindrome_order("AAAACACBAZZ"))
