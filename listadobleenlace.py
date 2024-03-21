from nodo import Node
from typing import TypeVar, Generic


T = TypeVar('T')


class List(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None
        self.numero = 0

    def recursivo_head(self):
        if self.numero == 0:
            self.__current = self.__head
            self.numero += 1
            self.recursivo_head()
        else:
            if self.__head.next is None:
                print(self.__head)
                self.__head = self.__current
                return ()
            else:
                print(self.__head)
                self.__head = self.__head.next
                self.numero += 1
                self.recursivo_head()

    def recursivo_tail(self):
        if self.numero == 0:
            self.__current = self.__tail
            self.numero += 1
            self.recursivo_tail()
        else:
            if self.__tail.prev is None:
                print(self.__tail)
                self.__tail = self.__current
                return ()
            else:
                print(self.__tail)
                self.__tail = self.__tail.prev
                self.numero += 1
                self.recursivo_tail()

    def append(self, data: T):
        if self.is_empty():
            new_node = Node(data, None, None)
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node = Node(data, None, self.__tail)
            self.__tail.next = new_node
            self.__tail = new_node
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

    def shift(self) -> T:
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista')
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
        current = self.__tail
        if self.is_empty():
            raise ReferenceError('No hay datos en la lista')
        elif self.__head is self.__tail:
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            previous = current.prev
            previous.next = None
            self.__tail = previous
            self.__size -= 1

            return current.data

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError('La pocición no existe')
        elif index == 0:
            return self.shift()
        elif index == (len(self)-1):
            return self.pop()
        else:
            current_node = self.find_at(index)
            previous_node = self.find_at(index - 1)
            next_node = current_node.next

            previous_node.next = next_node
            self.__size -= 1

            return current_node.data

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
        cont = 0
        for _ in self:
            cont += 1

        return cont
