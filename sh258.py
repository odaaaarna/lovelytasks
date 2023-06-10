def F (num):
    while num > 9:
        k = 0
        while num:
            k += num % 10
            num = num // 10
        num = k
    return num
print(F(0))
