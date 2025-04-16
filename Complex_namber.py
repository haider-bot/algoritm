def parse_complex(s):
    # Удаляем пробелы и разбиваем по 'i'
    s = s.replace(' ', '').replace('−', '-')
    if '+i' in s:
        real, imag = s.split('+i')
        sign = 1
    elif '-i' in s[1:]:  # Проверка после первого символа, чтобы не спутать с отрицательным числом
        real, imag = s.split('-i')
        sign = -1
    else:
        raise ValueError("Неверный формат. Используйте формат a + i*b или a - i*b")

    return int(real), sign * int(imag)

def add(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def subtract(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def multiply(c1, c2):
    # (a + ib)(c + id) = (ac - bd) + i(ad + bc)
    a, b = c1
    c, d = c2
    real = a * c - b * d
    imag = a * d + b * c
    return (real, imag)

def format_complex(c):
    a, b = c
    sign = '+' if b >= 0 else '-'
    return f"{a} {sign} i*{abs(b)}"

# Основной блок
input1 = input("Введите первое комплексное число (в формате a + i*b): ")
input2 = input("Введите второе комплексное число (в формате a + i*b): ")

z1 = parse_complex(input1)
z2 = parse_complex(input2)

sum_result = add(z1, z2)
diff_result = subtract(z1, z2)
prod_result = multiply(z1, z2)

print("Результаты в виде кортежей (действительная, мнимая):")
print("Сумма:      ", sum_result)
print("Разность:   ", diff_result)
print("Произведение:", prod_result)

print("\nВ красивом виде:")
print("Сумма:      ", format_complex(sum_result))
print("Разность:   ", format_complex(diff_result))
print("Произведение:", format_complex(prod_result))

# примеры, чтоб долго не придумывать
# 2 + i3
# 1 - i2

"""
Работа принтов

Введите первое комплексное число (в формате a + i*b): 2 + i3
Введите второе комплексное число (в формате a + i*b): 1 - i2
Результаты в виде кортежей (действительная, мнимая):
Сумма:       (3, 1)
Разность:    (1, 5)
Произведение: (8, -1)

В красивом виде:
Сумма:       3 + i*1
Разность:    1 + i*5
Произведение: 8 - i*1

"""