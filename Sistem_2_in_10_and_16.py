def convert_binary():
    binary_str = input("Введите число в двоичной системе: ")

    # Проверка, что ввод содержит только 0 и 1
    if not all(ch in '01' for ch in binary_str):
        print("Ошибка: Введите корректное двоичное число.")
        return

    decimal = int(binary_str, 2) # получаем число в двоичной системе, переводим в десятичную
    hexadecimal = hex(decimal)[2:].upper()  # получаем число в десятичной системе, переводим в шестнадцетиричную

    print(f"Десятичная система: {decimal}")
    print(f"Шестнадцатеричная система: {hexadecimal}")

# Пример запуска
convert_binary()
