import json
import os
#Дмитрук Яны
print("start code")
FILE_NAME = 'data.json'      # имя файла для хранения данных

operations_count = 0         # счетчик выполненных операций

def load_data():             # загружает данные из файла
    if os.path.exists(FILE_NAME):    # проверяет существование файла
        with open(FILE_NAME, 'r', encoding='utf-8') as file:     # открывает файл для чтения
            return json.load(file)   # возвращает данные из файла
    return []                # возвращает пустой список если файла нет

def save_data(data):         # сохраняет данные в файл
    with open(FILE_NAME, 'w', encoding='utf-8') as file:     # открывает файл для записи
        json.dump(data, file, ensure_ascii=False, indent=2)  # записывает данные с форматированием

def show_all_records():      # показывает все записи
    data = load_data()       # загружает данные
    if not data:             # проверяет есть ли записи
        print("\nНет записей в базе данных.")    # сообщение если данных нет
        return
    
    print("\n=== ВСЕ ЗАПИСИ ===")     # заголовок
    for i, record in enumerate(data, 1):    # перебирает все записи
        print(f"\nЗапись #{i}:")      # номер записи
        for key, value in record.items():   # перебирает поля записи
            print(f"  {key}: {value}")      # выводит поле и значение

def find_record_by_id():     # ищет запись по ID
    data = load_data()       # загружает данные
    if not data:             # проверяет есть ли записи
        print("\nНет записей в базе данных.")    # сообщение если данных нет
        return
    
    try:                     # обработка ввода
        search_id = int(input("\nВведите ID для поиска: "))  # запрашивает ID
    except ValueError:       # если введено не число
        print("Ошибка: ID должен быть числом.")  # сообщение об ошибке
        return
    
    found = False            # флаг найденной записи
    for i, record in enumerate(data, 1):    # перебирает записи
        if record.get('id') == search_id:   # сравнивает ID
            print(f"\nНайдена запись #{i}:")    # выводит номер найденной записи
            for key, value in record.items():   # перебирает поля записи
                print(f"  {key}: {value}")      # выводит поле и значение
            found = True             # устанавливает флаг
            break                    # прерывает поиск
    
    if not found:            # если запись не найдена
        print(f"\nЗапись с ID={search_id} не найдена.")  # сообщение об ошибке

def add_record():            # добавляет новую запись
    data = load_data()       # загружает данные
    
    print("\n=== ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ ===")  # заголовок
    
    try:                     # обработка ввода ID
        new_id = int(input("Введите ID: "))     # запрашивает новый ID
    except ValueError:       # если введено не число
        print("Ошибка: ID должен быть числом.")  # сообщение об ошибке
        return
    
    for record in data:      # проверяет существующие записи
        if record.get('id') == new_id:   # если ID уже существует
            print(f"Ошибка: запись с ID={new_id} уже существует.")  # сообщение об ошибке
            return
    
    name = input("Введите имя: ")        # запрашивает имя
    age = input("Введите возраст: ")     # запрашивает возраст
    city = input("Введите город: ")      # запрашивает город
    
    new_record = {           # создает новую запись
        'id': new_id,        # добавляет ID
        'name': name,        # добавляет имя
        'age': age,          # добавляет возраст
        'city': city         # добавляет город
    }
    
    data.append(new_record)  # добавляет запись в список
    save_data(data)          # сохраняет данные
    
    print(f"Запись с ID={new_id} успешно добавлена.")  # сообщение об успехе
    global operations_count  # обращается к глобальной переменной
    operations_count += 1    # увеличивает счетчик операций

def delete_record():         # удаляет запись
    data = load_data()       # загружает данные
    if not data:             # проверяет есть ли записи
        print("\nНет записей в базе данных.")    # сообщение если данных нет
        return
    
    try:                     # обработка ввода
        delete_id = int(input("\nВведите ID записи для удаления: "))  # запрашивает ID для удаления
    except ValueError:       # если введено не число
        print("Ошибка: ID должен быть числом.")  # сообщение об ошибке
        return
    
    found = False            # флаг найденной записи
    for i, record in enumerate(data):    # перебирает записи
        if record.get('id') == delete_id:   # сравнивает ID
            deleted_record = data.pop(i)    # удаляет запись по индексу
            save_data(data)          # сохраняет обновленные данные
            print(f"\nЗапись с ID={delete_id} успешно удалена.")  # сообщение об успехе
            print("Удаленная запись:")      # заголовок
            for key, value in deleted_record.items():   # перебирает поля удаленной записи
                print(f"  {key}: {value}")  # выводит поле и значение
            found = True             # устанавливает флаг
            global operations_count  # обращается к глобальной переменной
            operations_count += 1    # увеличивает счетчик операций
            break                    # прерывает поиск
    
    if not found:            # если запись не найдена
        print(f"\nЗапись с ID={delete_id} не найдена.")  # сообщение об ошибке

def exit_program():          # завершает программу
    print(f"\n=== ВЫХОД ИЗ ПРОГРАММЫ ===")  # заголовок
    print(f"Количество выполненных операций с записями: {operations_count}")  # выводит счетчик
    print("До свидания!")    # прощание
    exit()                   # завершает программу

def show_menu():             # показывает меню
    print("\n" + "="*40)    # верхняя граница
    print("ГЛАВНОЕ МЕНЮ")   # заголовок меню
    print("="*40)           # разделитель
    print("1. Вывести все записи")         # пункт 1
    print("2. Вывести запись по полю (ID)")# пункт 2
    print("3. Добавить запись")            # пункт 3
    print("4. Удалить запись по полю (ID)")# пункт 4
    print("5. Выйти из программы")         # пункт 5
    print("="*40)           # нижняя граница

def initialize_data():       # инициализирует начальные данные
    data = load_data()       # загружает данные
    if len(data) >= 5:       # проверяет достаточно ли записей
        return               # возвращает если достаточно
    
    initial_data = [         # создает начальные данные
        {'id': 1, 'name': 'Иван Иванов', 'age': 25, 'city': 'Москва'},          # запись 1
        {'id': 2, 'name': 'Петр Петров', 'age': 30, 'city': 'Санкт-Петербург'}, # запись 2
        {'id': 3, 'name': 'Анна Сидорова', 'age': 22, 'city': 'Казань'},        # запись 3
        {'id': 4, 'name': 'Мария Кузнецова', 'age': 28, 'city': 'Новосибирск'}, # запись 4
        {'id': 5, 'name': 'Алексей Смирнов', 'age': 35, 'city': 'Екатеринбург'} # запись 5
    ]
    
    save_data(initial_data)  # сохраняет начальные данные
    print("База данных инициализирована с 5 записями.")  # сообщение об инициализации

def main():                  # главная функция программы
    initialize_data()        # инициализирует данные
    
    while True:              # бесконечный цикл
        show_menu()          # показывает меню
        
        try:                 # обработка ошибок
            choice = input("Выберите пункт меню (1-5): ")  # запрашивает выбор
            
            if choice == '1':           # если выбран пункт 1
                show_all_records()      # показывает все записи
            elif choice == '2':         # если выбран пункт 2
                find_record_by_id()     # ищет запись по ID
            elif choice == '3':         # если выбран пункт 3
                add_record()            # добавляет запись
            elif choice == '4':         # если выбран пункт 4
                delete_record()         # удаляет запись
            elif choice == '5':         # если выбран пункт 5
                exit_program()          # выходит из программы
            else:                       # если выбор некорректен
                print("Ошибка: выберите пункт от 1 до 5.")  # сообщение об ошибке
        
        except KeyboardInterrupt:       # если нажат Ctrl+C
            print("\n\nПрограмма прервана пользователем.")  # сообщение
            exit_program()              # выходит из программы
        
        except Exception as e:          # если произошла другая ошибка
            print(f"Произошла ошибка: {e}")  # выводит ошибку

if __name__ == "__main__":  # проверяет что файл запущен напрямую
    main()                  # запускает главную функцию

print("end code")