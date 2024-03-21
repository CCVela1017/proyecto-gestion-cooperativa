from __future__ import annotations
from typing import TypeVar, Generic  # Variables genericas


T = TypeVar("T")  # trabaja con cualquier dato pero del mismo tipo


class Node(Generic[T]):
    def __init__(self, data: T, next_node=None):  # data depende del caso pero se deja generico.
        self.__data = data  # privado no se puede heredar.
        self.__next: Node | None = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next

    def __str__(self):
        return str(self.__data)