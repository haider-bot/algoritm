"""
Памятка по индексам

Index       Namber

0           1
1           2
2           3
...         ...

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Создание связного списка из массива
def build_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Печать связного списка
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n") # по приколу
        current = current.next

# Удаление по индексу
def delete_at_index(head, index):
    if index < 0:
        return head  # Ничего не делаем

    # Удаление головы
    if index == 0 and head:
        return head.next

    current = head
    prev = None
    i = 0

    while current and i < index:
        prev = current
        current = current.next
        i += 1

    if current is None:
        return head  # Индекс вне диапазона

    prev.next = current.next
    return head

# Пример использования:
head = build_linked_list([1, 2, 3, 4])
print("До удаления:")
print_linked_list(head)

head = delete_at_index(head, 2)
print("После удаления элемента с индексом 2:")
print_linked_list(head)

