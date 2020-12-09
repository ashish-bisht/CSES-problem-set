def two_sets(n):

    sum = n*(n + 1)//2
    if sum % 2 != 0:
        return "False"

    else:
        print("Hell yes we can")

        first_list = []
        second_list = []

        sum = sum//2

        while n > 0:
            if sum - n >= 0:
                first_list.append(n)
                sum -= n

            else:
                second_list.append(n)

            n -= 1

        print(len(first_list))
        print(*first_list)
        print(len(second_list))
        print(*second_list)


print(two_sets(7))
