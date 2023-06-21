# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv

# user=["ferstname","secondname","phone","discription"]
# phone_dir = {1:["ferstname","secondname","phone","discription"],2:["ferstname","secondname","phone","discription"]}

    # phone_book = {1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
    #         2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
    #         3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
    #         4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
    #         5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
    #         6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
    #         }  

import os.path as path1

def get_user() -> list:
    user =[]
    user.append(input("Введите фамилию: "))
    user.append(input("Введите имя: "))
    user.append(input("Введите номер телефона: "))
    user.append(input("Введите комментарий: "))
    return user

def create(phone_book_local: dict,user:list) -> dict:
    if len(phone_book_local) == 0:              
        idc =  1
    else:
        idc = max(phone_book_local.keys())+1
    phone_book_local[idc] = user
    return phone_book_local
    
def search_user(phone_book_local: dict):
    surname = input("Введите начальные буквы фамилии: ")
    for idc, user in phone_book_local.items():
        if ((user[0]).lower()).startswith(surname.lower()) == True:
            print(*phone_book_local[idc])
            return idc

def delete_user(phone_book_local, idc)-> dict:
    del phone_book_local[idc]
    return phone_book_local

def update_user(phone_book_local, idc)-> dict:
    while True:
        print("Введите 1, чтобы изменить фамилию")
        print("Введите 2, чтобы изменить имя")
        print("Введите 3, чтобы изменить телефон")
        print("Введите 4, чтобы изменить комментарий")
        print("Введите 0, чтобы выйти")
        change_menu = int(input("Выберите действие: "))
        if change_menu == 0:
            break
        else: 
            new_value = input("Введите новое значение: ")
            phone_book_local[idc][change_menu-1] = new_value
            print(f"Новая запись: {phone_book_local[idc]}")
    return phone_book_local        


def export_in_file(phone_book_local: dict):
    file_name = input("Введите имя файла: ") + '.csv'
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    file_path = path1.join(MAIN_DIR, file_name)
    with open(file_path, mode="w", encoding="utf-8") as file:
        for idc, user in phone_book_local.items():
            file.write(f"{user[0]}, {user[1]}, {user[2]}, {user[3]}\n")

def import_from_file() -> dict:
    file_name = input("Введите имя файла: ") + '.csv'
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    file_path = path1.join(MAIN_DIR, file_name)
    phone_book_local = dict()
    with open(file_path, mode="r", encoding="utf-8") as file:
        key_count = 1
        for line in file:
            phone_book_local[key_count] = line.strip().split(', ')
            key_count+=1
    return phone_book_local
                                           
def menu():
    phone_book= dict()    
    while True:
        print("Введите 1, чтобы добавить нового пользователя")
        print("Введите 2, чтобы отобразить весь справочник")
        print("Введите 3, чтобы найти пользователя")
        print("Введите 4, чтобы отредактировать пользователя")
        print("Введите 5, чтобы удалить пользователя")
        print("Введите 6, чтобы экспортировать данные в файл")
        print("Введите 7, чтобы импортировать данные из файла")
        print("Введите 0, чтобы выйти из программы")
        menu_item = int(input("Выберите действие: "))
        if menu_item == 0:
            break
        if menu_item == 1:
            user = get_user()
            phone_book = create(phone_book,user)
        if menu_item == 2:
            print(phone_book)
        if menu_item == 3:
            search_user(phone_book)
        if menu_item == 4:
            inx = search_user(phone_book)
            phone_book = update_user(phone_book, inx)
        if menu_item == 5:
            inx = search_user(phone_book)
            phone_book = delete_user(phone_book, inx)
        if menu_item == 6:
            export_in_file(phone_book)    
        if menu_item == 7:
            phone_book = import_from_file()
                
menu()

