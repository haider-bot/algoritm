def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего — меняем местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Пример использования:
nums = [5, 2, 9, 1, 5, 6]
sorted_nums = bubble_sort(nums.copy())

print("Исходный массив:", nums)
print("Отсортированный массив:", sorted_nums)
