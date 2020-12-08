def weird_algo(num):

    while True:
        print(num)
        if num == 1:
            break
        if num % 2 == 0:
            num = num//2

        else:
            num = (num*3) + 1


print(weird_algo(3))  # 3 , 10, 5, 16, 8, 4, 2,1
