import typing as t
from typing import Any
from Exc import Exceptions


class Node:
    def __init__(self, info: t.Any):
        self.info = info
        self.next = None


class SinglyLinkedList:
    def __init__(self, name: str, *args) -> None:
        self.name = name
        self.head = None
        self.tail = None
        self.fill_list(args)

    def fill_list(self, args):
        for arg in args:
            self.append(arg)

    def is_empty(self) -> bool:
        return self.head is None

    def _is_index_error(self, index: int) -> bool:
        current_index = self.__len__() - 1
        if index < current_index:
            return True
        return False

    def append(self, info: t.Any) -> None:
        new_node = Node(info)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def _remove_first_element(self) -> None:
        self.head = self.head.next

    def _remove_last_element(self) -> None:
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    def find(self, find_info: t.Any) -> int:
        index: int = 0
        current = self.head
        while current is not None:
            current_info = current.info
            if current_info == find_info and type(current_info) == type(find_info):
                return index
            current = current.next
            index += 1
        return -1

    def __delitem__(self, index: int) -> None:
        if index == 0:
            self._remove_first_element()
            return
        if index == self.__len__() - 1:
            self._remove_last_element()
            return
        current_index: int = 0
        slow: Node = self.head
        fast: Node = slow.next
        while fast:
            if current_index + 1 == index:
                slow.next = fast.next
                return
            slow = fast
            fast = slow.next
            current_index += 1
        raise Exceptions.IndexError(self.name, current_index, index)

    def __getitem__(self, index: int) -> Any | None:
        current = self.head
        current_index: int = 0
        while current is not None:
            if current_index == index:
                return current.info
            current = current.next
            current_index += 1
        raise Exceptions.IndexError(self.name, current_index, index)

    def __len__(self) -> int:
        return self._get_len()

    def _get_len(self) -> int:
        counter: int = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def display(self) -> None:
        current: Node = self.head
        while current is not None:
            print(current.info)
            current = current.next
