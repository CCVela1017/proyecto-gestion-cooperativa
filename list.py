from node import Node
from typing import TypeVar, Generic

T = TypeVar("T")


class List(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None   # la cabeza señala a un nodo o nulo (guardar)
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None

    # Metodos de insercion

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

    def prepend(self, data: T):
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__head = new_node
            self.__size += 1

    def insert_at(self, data: T, index: int):  # Insertar en cualquier posicion
        if index == 0:
            self.prepend(data)
        elif index == len(self) - 1:
            self.append(data)
        elif index < 0 or index > len(self):
            raise IndexError("La posicion es inválida")
        else:
            new_node = Node(data)
            previous_node = self.find_at(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.__size += 1

    # == compara valores
    # is compara posicion de memoria

    # Metodo de eliminacion
    def shift(self) -> T:   # Eliminar al inicio (T es para doverlver la data)
        if self.is_empty():  # si esta vacio
            raise ReferenceError("No hay datos en la lista")
        elif self.__head is self.__tail: # si la cabeza es igual a la cola
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head  # situa un puntero en la cabeza
            self.__head = current.next  # mueve la cabeza al siguiente
            current.next = None  # elimina enlace
            self.__size -= 1

            return current.data

    def pop(self) -> T:  # Eliminar al final
        if self.is_empty():
            raise ReferenceError("No hay datos en la lista")
        if self.__head is self.__tail:
            current = self.__tail
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data

        else:
            current = self.__tail
            previous = self.find_at(len(self) - 2)  # nodo anterior al que esta en cola
            self.__tail = previous  # la cola sera el nodo anterior
            previous.next = None
            self.__size -= 1

            return current.data

    def remove_at(self, index: int) -> T:  # Eliminar en cualquier posicion
        if index < 0 or index >= len(self):
            raise IndexError("La posicion no existe")
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

    # Metodo de busqueda
    def find_at(self, index: int) -> Node[T]:  # Buscar por posicion
        current_index = 0
        current = self.__head

        while True:
            if current is None:
                break
            if current_index == index:
                return current
            else:
                current = current.next
                current_index += 1

        raise IndexError("La posicion no existe")

    # Metodos auxiliares

    def is_empty(self):  # Si esta vacio
        return self.__head is None and self.__tail is None   # lista vacia

    def __iter__(self):
        self.__current = self.__head  # indica donde comienza la iteracion
        return self

    def __next__(self):  # navega al siguiente elemento o detener la iteracion
        if self.__current is None:
            raise StopIteration

        data = self.__current.data
        self.__current = self.__current.next

        return data

    def __len__(self):  # Para saber el tamaño de la estrutura de datos(longitud)
        cont = 0

        for _ in self:  # _ significa ignorar la variable que no se utilizara
            cont += 1

        return cont
