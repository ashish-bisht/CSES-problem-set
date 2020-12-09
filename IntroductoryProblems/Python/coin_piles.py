def coin_piles(coin_a, coin_b):

    while coin_a > 0 and coin_b > 0:
        if coin_a >= coin_b:
            coin_a -= 2
            coin_b -= 1

        else:
            coin_b -= 2
            coin_a -= 1
    return "Yes" if coin_a == coin_b == 0 else "No"


print(coin_piles(2, 1))
print(coin_piles(2, 2))
print(coin_piles(3, 3))
