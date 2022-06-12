# 13_1
def f(ls):
    ls1 = []
    for i in ls:
        summ = 0
        while i > 0:
            num = i % 10
            summ += num
            i //= 10
        ls1.append(summ)
    return sorted(ls1)


ls = [int(i) for i in input().split()]
print(f(ls))


# 13_2
def f(a):
    if a <= -2:
        return 1 - (a + 2)**2
    elif -2 < a <= 2:
        return - a / 2
    return (a - 2)**2 + 1


print(f(a))


# 13_3
def f(ls):
    a = []
    for i in ls:
        if i % 2 == 0:
            i = i // 2
            a.append(i)
    return a


ls = [int(i) for i in input().split()]
print(f(ls))