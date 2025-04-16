def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние отсортированных половин
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Пока в обеих частях есть элементы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Добавим оставшиеся элементы (если остались)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Пример использования:
arr = [5, 3, 8, 4, 2, 7, 1, 6]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
