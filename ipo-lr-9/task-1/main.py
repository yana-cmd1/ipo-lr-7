#Дмитрук Яны
import json
import os 
print("start code")
 

file_name = 'data.json' # определение имени файла
operation_counter = 0 # инициализация счетчика операций

def fetch_data(): # функция получения данных
    if os.path.exists(file_name): # проверка существования файла
        with open(file_name, 'r', encoding='utf-8') as f: # открытие файла для чтения
            return json.load(f) # возврат данных из файла
    return [] # возврат пустого списка

def store_data(info): # функция сохранения данных
    with open(file_name, 'w', encoding='utf-8') as f: # открытие файла для записи
        json.dump(info, f, ensure_ascii=False, indent=2) # запись данных

def display_records(): # отображение всех записей
    records = fetch_data() # загрузка данных
    if not records: # проверка на пустоту
        print("\nбаза данных пуста") # сообщение
        return
    
    print("\n=== все записи ===") # заголовок
    for index, item in enumerate(records, 1): # перебор записей
        print(f"\nзапись #{index}:") # вывод номера
        for k, v in item.items(): # перебор полей
            print(f"  {k}: {v}") # вывод значений

def search_by_identifier(): # поиск по id
    records = fetch_data() # загрузка данных
    if not records: # проверка на пустоту
        print("\nнет доступных записей") # сообщение
        return
    
    try: # обработка ввода
        target_id = int(input("\nвведите идентификатор для поиска: ")) # запрос
    except ValueError: # ошибка ввода
        print("некорректный идентификатор - требуется число") # сообщение
        return
    
    for idx, item in enumerate(records, 1): # поиск по записям
        if item.get('id') == target_id: # сравнение id
            print(f"\nнайдена запись #{idx}:") # вывод результата
            for k, v in item.items(): # перебор полей
                print(f"  {k}: {v}") # вывод значений
            return # выход
    
    print(f"\nзапись с идентификатором {target_id} отсутствует") # не найдено

def insert_new_record(): # добавление записи
    data = fetch_data() # загрузка данных
    
    print("\n=== добавление новой записи ===") # заголовок
    
    try: # обработка ввода
        new_id_val = int(input("введите идентификатор: ")) # запрос id
    except ValueError: # ошибка ввода
        print("идентификатор должен быть числовым значением") # сообщение
        return
    
    for entry in data: # проверка уникальности
        if entry.get('id') == new_id_val: # если id существует
            print(f"идентификатор {new_id_val} уже используется") # сообщение
            return
    
    name_val = input("введите имя: ") # запрос имени
    age_val = input("введите возраст: ") # запрос возраста
    location = input("введите местоположение: ") # запрос города
    
    new_entry = { # создание записи
        'id': new_id_val, # id
        'name': name_val, # имя
        'age': age_val, # возраст
        'city': location # город
    }
    
    data.append(new_entry) # добавление в список
    store_data(data) # сохранение данных
    
    print(f"добавлена запись с идентификатором {new_id_val}") # сообщение
    global operation_counter # глобальная переменная
    operation_counter += 1 # увеличение счетчика

def remove_entry(): # удаление записи
    data = fetch_data() # загрузка данных
    if not data: # проверка на пустоту
        print("\nбаза данных не содержит записей") # сообщение
        return
    
    try: # обработка ввода
        remove_id = int(input("\nвведите идентификатор записи для удаления: ")) # запрос
    except ValueError: # ошибка ввода
        print("требуется числовой идентификатор") # сообщение
        return
    
    for position, entry in enumerate(data): # поиск записи
        if entry.get('id') == remove_id: # если id совпадает
            removed_item = data.pop(position) # удаление из списка
            store_data(data) # сохранение изменений
            print(f"\nудалена запись с идентификатором {remove_id}") # сообщение
            print("удаленная информация:") # заголовок
            for k, v in removed_item.items(): # перебор полей
                print(f"  {k}: {v}") # вывод значений
            global operation_counter # глобальная переменная
            operation_counter += 1 # увеличение счетчика
            return # выход
    
    print(f"\nзапись с идентификатором {remove_id} не обнаружена") # не найдено

def terminate_app(): # завершение программы
    print(f"\n=== завершение работы ===") # заголовок
    print(f"выполнено операций: {operation_counter}") # вывод счетчика
    print("работа завершена") # прощание
    exit() # выход из программы

def menu_interface(): # отображение меню
    print("\n" + "="*40) # верхняя граница
    print("основное меню") # заголовок меню
    print("="*40) # разделитель
    print("1. показать все записи") # пункт 1
    print("2. найти запись по идентификатору") # пункт 2
    print("3. создать новую запись") # пункт 3
    print("4. удалить запись") # пункт 4
    print("5. завершить работу") # пункт 5
    print("="*40) # нижняя граница

def setup_initial_data(): # инициализация начальных данных
    current_data = fetch_data() # загрузка текущих данных
    if len(current_data) >= 5: # проверка количества записей
        return # выход если достаточно
    
    sample_data = [ # начальные данные
        {'id': 101, 'name': 'андрей павлов', 'age': 27, 'city': 'краснодар'}, # запись 1
        {'id': 102, 'name': 'елена волкова', 'age': 31, 'city': 'ростов'}, # запись 2
        {'id': 103, 'name': 'сергей орлов', 'age': 24, 'city': 'воронеж'}, # запись 3
        {'id': 104, 'name': 'ольга лебедева', 'age': 29, 'city': 'самара'}, # запись 4
        {'id': 105, 'name': 'дмитрий соколов', 'age': 33, 'city': 'уфа'} # запись 5
    ]
    
    store_data(sample_data) # сохранение начальных данных
    print("инициализирована база с пятью записями") # сообщение об инициализации

def program_loop(): # главный цикл программы
    setup_initial_data() # инициализация данных
    
    while True: # бесконечный цикл
        menu_interface() # вывод меню
        
        try: # обработка ошибок
            selection = input("укажите действие (1-5): ") # запрос выбора
            
            if selection == '1': # если выбрано 1
                display_records() # показать записи
            elif selection == '2': # если выбрано 2
                search_by_identifier() # поиск по id
            elif selection == '3': # если выбрано 3
                insert_new_record() # добавление записи
            elif selection == '4': # если выбрано 4
                remove_entry() # удаление записи
            elif selection == '5': # если выбрано 5
                terminate_app() # завершение программы
            else: # неверный выбор
                print("неверный выбор - используйте значения 1-5") # сообщение об ошибке
        
        except KeyboardInterrupt: # если нажат ctrl+c
            print("\n\nоперация прервана") # сообщение
            terminate_app() # завершение программы
        
        except Exception as err: # другие ошибки
            print(f"ошибка выполнения: {err}") # вывод ошибки

if __name__ == "__main__": # проверка запуска файла напрямую
    program_loop() # запуск главного цикла

print("end code")
