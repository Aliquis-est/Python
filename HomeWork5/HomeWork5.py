
# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения.
# Циклы использовать нельзя

#     Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16

def exponentiation(num: int, m: int) -> int:
    
    if m == 0:
        return 1
    return exponentiation(num, m-1)*num

digit1= int(input("Введите число, которое необходимо возвести в степень: "))
digit2 = int(input("Введите степень: "))

print(exponentiation(digit1, digit2))



# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3

# def summation(n:int, m:int) -> int:
    
#     if m == 0:
#         return n
#     return summation(n + 1, m - 1)

# digit1= int(input("Введите первое число: "))
# digit2 = int(input("Введите второе число: "))
# print(summation(digit1, digit2))