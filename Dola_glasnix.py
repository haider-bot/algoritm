def vowel_ratio(text):
    vowels = "аеёиоуыэюяaeiou"  # Русские и английские гласные (без учета регистра)
    total_letters = 0
    vowel_count = 0

    for char in text.lower():
        if char.isalpha():
            total_letters += 1
            if char in vowels:
                vowel_count += 1

    if total_letters == 0:
        return 0.0  # если букв вообще не было
    return vowel_count / total_letters


# принты и ввод
user_input = input("Введите строку: ")
ratio = vowel_ratio(user_input)
print(f"Доля гласных букв: {ratio:.2f}")
