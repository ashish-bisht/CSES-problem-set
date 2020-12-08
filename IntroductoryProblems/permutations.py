def permutations(num):
    if num <= 3:
        return "No Solution"
    beautiful = [-1] * num
    left = 0
    right = num//2
    cur_num = num
    while left < right and right < num:
        if cur_num % 2 == 0:
            beautiful[left] = cur_num
            left += 1
        else:
            beautiful[right] = cur_num
            right += 1

        cur_num -= 1
    return beautiful


print(permutations(5))  # 4,2,5,3,1
print(permutations(6))
print(permutations(3))
