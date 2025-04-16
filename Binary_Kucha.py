"""
    Сравниваем новый (добавленный) элемент с родительским элементом (эллемент выше)
    Если элемент меньше (родительского элемента), меняем местами и продолжаем проверку вверх по дереву
    Если не меньше => выходим, свойства кучи соблюдены

"""


def insert_to_heap(heap, value):
    # Добавляем элемент в конец кучи
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

    return heap

heap = [1, 3, 5, 7, 9, 6]
new_element = 2

updated_heap = insert_to_heap(heap, new_element)
print(updated_heap)  # [1, 3, 2, 7, 9, 6, 5]
