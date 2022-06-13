import random
# 13.4

def f(step, start, stop):
    sp = []
    while step != 0:
        a = random.randint(start, stop)
        step -= 1
        sp.append(a)
    return sp


step, start, stop = int(input()), int(input()), int(input())
print(f(step, start, stop))

# 13.5

