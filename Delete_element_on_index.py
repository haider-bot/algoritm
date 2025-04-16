class Node:
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Указатель на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            print("Список пуст.")
            return None

        current = self.head

        # Если удаляем первый элемент (индекс 0)
        if index == 0:
            self.head = current.next  # Сдвигаем голову списка на следующий узел
            return self.head

        # Пройдем по списку до нужного индекса
        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        # Если индекс вне диапазона
        if current is None:
            print("Индекс за пределами списка.")
            return None

        # Удаление элемента
        prev.next = current.next
        return self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Пример использования:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Исходный список:")
linked_list.print_list()

# Удаляем элемент с индексом 2 (элемент со значением 3)
linked_list.delete_at_index(2)

print("Список после удаления элемента с индексом 2:")
linked_list.print_list()

# Удаляем первый элемент (с индексом 0)
linked_list.delete_at_index(0)

print("Список после удаления первого элемента:")
linked_list.print_list()


"""
Принты

Исходный список:
1 -> 2 -> 3 -> 4 -> None
Список после удаления элемента с индексом 2:
1 -> 2 -> 4 -> None
Список после удаления первого элемента:
2 -> 4 -> None

"""