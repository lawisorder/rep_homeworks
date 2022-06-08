# n = [int(i) for i in input().split()]
# a = n.index(min(n))
# b = n.index(max(n))
# n[a], n[b] = n[b], n[a]
# print(*n)
# 
# n = input().split()
# summ = n.count('a') + n.count('an') + n.count('the') + n.count('A') + n.count('An') + n.count('The')
# print(f'Общее количество артиклей: {summ}')

# n = [int(i) for i in input().split()]
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)

# print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and (int(i) ** 2) % 10 != 4], sep=' ')

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9]

n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] <= a[j+1]:
            continue
        else:
            a[j], a[j+1] = a[j+1], a[j]
print(a)