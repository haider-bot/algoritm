def binary_converter():
    while True:
        binary_str = input("Введите число в двоичной системе: ").strip()

        # Проверка, состоит ли строка только из 0 и 1
        if all(char in '01' for char in binary_str) and binary_str:
            decimal = int(binary_str, 2)
            hexadecimal = hex(decimal)[2:].upper()  
            print(f"Десятичная система: {decimal}")
            print(f"Шестнадцатеричная система: {hexadecimal}")
            break
        else:
            print("Неверный ввод! Введите только 0 и 1.")

# Пример запуска
binary_converter()
