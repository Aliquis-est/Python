
# [26] Напишите рекурсивную функцию для возведения числа a в степень b. 

# def exponentiation(num: int, m: int) -> int:
    
#     if m == 0:
#         return 1
#     return exponentiation(num, m-1)*num

# digit1= int(input("Введите число, которое необходимо возвести в степень: "))
# digit2 = int(input("Введите степень: "))

# print(exponentiation(digit1, digit2))



# [28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    

# def summation(n:int, m:int) -> int:
    
#     if m == 0:
#         return n
#     return summation(n + 1, m - 1)

# digit1= int(input("Введите первое число: "))
# digit2 = int(input("Введите второе число: "))
# print(summation(digit1, digit2))