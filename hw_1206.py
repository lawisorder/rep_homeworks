import random
import math


#  13.4
#
# def f(step, start, stop):
#     sp = []
#     while step != 0:
#         a = random.randint(start, stop)
#         step -= 1
#         sp.append(a)
#     return sp
#
#
# step, start, stop = int(input()), int(input()), int(input())
# print(f(step, start, stop))

# 13.5

# pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
#             'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
#             'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
#
# def menu(qwest):
#     return answer
#
# buy = input('Какой торт Вы хотели бы приобрести: ').lower()
# look = input('Что Вы хотели бы уточнить: ').lower()
#
# for k, v in pastry.items():
#     if k == buy:
#         answer = f"торт {k} состоит из {v[0]}"
#         print(menu("описание"))
#
#         answer = f"торт {k} стоит рублей {v[1]}"
#         print(menu("цена"))
#
#         answer = f"торта {k} осталось грамм {v[-1]}"
#         print(menu('"количество":'))

        # elif look == "купить":
        #     gr = int(input("Сколько торта Вам положить: "))
        #     return f"к оплате {v[1] * gr / 100}, торта {k} осталось грамм {v[-1] - gr}"




# 13.6
# вариант без рекурсии

# def find_factorial(num):
#     a = 1
#     for i in range(1, num+1):
#         a *= i
#     return a
#
# print(find_factorial(int(input())))

# вариант с рекурсией

# def f(x):
#     if x == 1:
#         return 1
#     return f(x-1)*x
#
# print(f(int(input())))


# "хитрый" вариант

# print(math.factorial(int(input())))