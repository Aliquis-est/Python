import math


# x = int(input("Введите размер шоколадки по вертикали (x): "))
# y = int(input("Введите размер шоколадки по горизонтали (y): "))
# k = int(input("Введите количество долек: "))

# if k % x == 0 or k % y == 0:
#     print("yes")
# else:
#     print("no")





# n = int(input("Введите число: "))
# result = 1
# i = 2
# while i <= n:
#     result *= i # result = result * i
#     i += 1
# print(f'{n}! = {result}')


# n = int(input("Введите число: "))
# x0 = 0
# x1 = 1
# x = 0
# i = 2
# while x < n:
#     x = x0 + x1 
#     x0 = x1 
#     x1 = x 
#     i += 1
#     if x > n:
#         i = 0

# if i == 0:
#     print(-1)
# else:
#     print(i)



# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count_days = 0
# for i in range(n):
#     x = int(input("Введите среднюю температуру дня: "))
#     if x > 0:
#         count += 1
#     else:
#         count = 0

#     if max_count_days < count:
#         max_count_days = count
# print(max_count_days)