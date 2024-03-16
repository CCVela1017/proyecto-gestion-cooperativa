from node import Node
from typing import TypeVar, Generic

T = TypeVar('T')


class List(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None

    # Métodos de inserción
    def prepend(self, data: T):
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__head = new_node
            self.__size += 1

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__size += 1

    def insert_at(self, data: T, index: int):
        if index == 0:
            self.prepend(data)
        elif index == len(self) - 1:
            self.append(data)
        elif index < 0 or index > len(self):
            raise IndexError('La posición es inválida')
        else:
            new_node = Node(data)
            previous_node = self.find_at(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.__size += 1

    # Métodos de busqueda
    def find_at(self, index: int) -> Node[T]:
        current_index = 0
        current = self.__head
        while True:
            if current is None:
                break
            elif current_index == index:
                return current
            else:
                current = current.next
                current_index += 1

        raise IndexError('La posición no extiste')

    # Métodos auxiliares
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

    def __len__(self):
        size = 0
        for _ in self:
            size += 1

        return size

    # Métodos de eliminación

    def shift(self) -> T:
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista.')
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
            self.__size -= 1
            return current.data

    def pop(self) -> T:
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
            previous = self.find_at(len(self) - 2)
            self.__tail = previous
            previous.next = None
            self.__size -= 1
            return current.data

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError('La posición no existe')
        elif index == 0:
            return self.shift()
        elif index == len(self) - 1:
            return self.pop()
        else:
            current_node = self.find_at(index)
            previous_node = self.find_at(index - 1)
            next_node = current_node.next
            previous_node.next = next_node
            current_node.next = None
            self.__size -= 1
            return current_node.data
