def trailing_zeroes(n):
    zeroes = 0

    while n > 0:
        n = n//5
        zeroes += n

    return zeroes


print(trailing_zeroes(10))  # 2
print(trailing_zeroes(20))  # 4
