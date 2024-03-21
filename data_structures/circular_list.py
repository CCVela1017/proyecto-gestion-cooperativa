from typing import TypeVar, Generic
from data_structures.node import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__current: Node[T] | None = None
        self.__previous: Node[T] | None = None
        self.__size: int = 0

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__tail.next = self.__head
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__tail.next = self.__head
        self.__size += 1

    def shift(self) -> T:
        if self.is_empty():
            raise MemoryError('Subdesbordamiento de lista')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head
            self.__head = self.__head.next
            self.__current.next = None
            self.__tail.next = self.__head
            self.__size -= 1
            return current.data

    def pop(self) -> T:
        if self.is_empty():
            raise MemoryError('Subdesbordamiento de lista')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current
        else:
            current = self.__tail
            previous = self.find_at(self.__size - 2)
            self.__tail = previous
            self.__tail.next = self.__head
            current.next = None
            self.__size -= 1

            return current.data

    def insert_at(self, data: T, index: int):
        if index == 0:
            self.prepend(data)
        elif index == len(self):
            self.append(data)
        elif index < 0 or index > len(self):
            raise IndexError('La posición es inválida')
        else:
            new_node = Node(data)
            previous_node = self.find_at(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.__size += 1

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

    def __len__(self):
        return self.__size

    def find_at(self, index: int) -> Node[T]:
        current = self.__head
        for current_index in range(self.__size):
            if current_index == index:
                return current
            else:
                current = current.next
        raise IndexError('La posición no extiste')

    def is_empty(self) -> bool:
        return (self.__head is None and
                self.__tail is None)

    # DONDE EMPIEZA
    def __iter__(self):
        self.__current = self.__head
        self.__previous = self.__tail
        return self

    # MOVER HACIA EL SIGUIENTE
    def __next__(self):
        if self.__previous is not None:
            if self.__size == 1:
                self.__previous = None
                return self.__current.data
            else:
                if self.__previous is not self.__head:
                    data = self.__current.data
                    self.__current = self.__current.next
                    self.__previous = self.__current

                    return data
                else:
                    raise StopIteration
        else:
            raise StopIteration
