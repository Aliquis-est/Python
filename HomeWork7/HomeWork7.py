# 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# def count_vowel(text: str) -> int:
#     vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
#     count = 0
#     for item in vowels:
#         count += text.count(item)
#     return count


# def rhythm(text: str) -> bool:
#     words = text.split()
#     count = count_vowel(words[0])
#     if count == 0 : 
#         return False

#     for i in range(1, len(words)):
#         if count != count_vowel(words[i]):
#             return False
#     return True


# print(rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам"))
# print(rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
# print(rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
# print(rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
# print(rhythm("Пам-парам-пурум Пум-пурум-карам"))




# 32: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.

# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256

# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36


def print_operation_table(func, num_rows, num_columns):
    for idx_rows in range(1, num_rows+1):
        begin_string = (f"")
        for idx_columns in range(1, num_columns+1):
            begin_string += ((str(func(idx_rows, idx_columns))).rjust(3))
        print(begin_string)
    print('\n')
    


print_operation_table(lambda x, y: x**y, 4, 4)
print_operation_table(lambda x, y: x*y, 6, 6)