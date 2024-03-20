from data_structures.node import Node
from typing import TypeVar, Generic

T = TypeVar('T')


class DoubleList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__current: Node[T] | None = None
        self.__size = 0

    # Métodos para insertar

    def insert_at(self, data: T, index: int):
        if index == 0:
            self.prepend(data)
        elif index == len(self):
            self.append(data)
        elif index < 0 or index > len(self):
            raise IndexError('La posición es inválida')
        else:
            new_node = Node(data, None, None)
            current = self.search_by_index(index - 1)
            next_node = current.next
            next_node.prev = new_node
            new_node.next = next_node
            current.next = new_node
            new_node.prev = current
            self.__size += 1

    def prepend(self, data: T):
        if self.is_empty():
            new_node = Node(data, None, None)
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node = Node(data, self.__head, None)
            current = self.__head
            current.prev = new_node
            self.__head = new_node
            self.__size += 1

    def append(self, data: T):
        if self.is_empty():
            new_node = Node(data, None, None)
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node = Node(data, None, self.__tail)
            current = self.__tail
            current.next = new_node
            self.__tail = new_node
            self.__size += 1

    # Métodos auxiliares

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__head is None and self.__tail is None

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration

        data = self.__current.data
        self.__current = self.__current.next

        return data

    # Métodos para buscar
    def search_by_value(self, data: T):
        if self.is_empty():
            raise ReferenceError('ERROR: EL VALOR NO EXISTE')
        else:
            current = self.__head
            for i in range(self.__size):

                if current.data == data:
                    return current
                else:
                    current = current.next
            raise ReferenceError('ERROR: EL VALOR NO EXISTE')

    def search_by_index(self, index: int):
        j = 0
        if self.is_empty():
            raise ReferenceError('ERROR: El valor no existe')
        elif index > self.__size:
            raise IndexError('ERROR: La posición no existe')
        else:
            current = self.__head
            for i in range(self.__size):
                if i == index:
                    return current
                else:
                    current = current.next

    # Métodos para eliminar

    def delete_at(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError('La posición no existe')
        elif index == 0:
            return self.shift()
        elif index == len(self) - 1:
            return self.pop()
        else:
            current_node = self.search_by_index(index)
            previous_node = current_node.prev
            next_node = current_node.next
            previous_node.next = next_node
            next_node.prev = previous_node
            current_node.next = None
            current_node.prev = None
            self.__size -= 1
            return current_node.data

    def shift(self):
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista doble.')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head
            self.__head = current.next
            current.next = None
            self.__head.prev = None
            self.__size -= 1
            return current.data

    def pop(self):
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista.')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__tail
            previous = current.prev
            previous.next = None
            self.__tail = previous
            self.__size -= 1
            return current.data
