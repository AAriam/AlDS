"""Module containing queue data structures, such as FIFO, LIFO, and priority queues."""

from typing import Any, Callable, Optional, NoReturn
from .abc import Queue


class FIFOQueue(Queue):
    """A queue data structure with a first-in-first-out (FIFO) policy."""

    def __init__(self, init_queue: Optional[list] = None):
        if init_queue is None:
            self._data = []
        elif isinstance(init_queue, list):
            self._data = init_queue
        else:
            raise TypeError("Argument `init_queue` must be of type `list`.")
        return

    def __str__(self):
        return ", ".join([str(elem) for elem in self._data])

    def __repr__(self):
        return f"{type(self).__name__}({self._data})"

    def push(self, element: Any):
        self._data.insert(0, element)
        return

    def pop(self):
        return self._data.pop()

    def has_element(self, elem: Any, key: Callable = lambda elem: elem) -> bool:
        for e in self._data:
            if key(e) == elem:
                return True
        return False

    @property
    def top(self) -> Any:
        return self._data[-1]

    @property
    def is_empty(self):
        return len(self._data) == 0


class LIFOQueue:
    """A queue data structure with a last-in-first-out (LIFO) policy, also known as a stack."""

    def __init__(self, init_queue: Optional[list] = None):
        if init_queue is None:
            self._data = []
        elif isinstance(init_queue, list):
            self._data = init_queue
        else:
            raise TypeError("Argument `init_queue` must be of type `list`.")
        return

    def __str__(self):
        return ", ".join([str(elem) for elem in self._data[-1::-1]])

    def push(self, element: Any) -> NoReturn:
        self._data.append(element)
        return

    def pop(self) -> Any:
        return self._data.pop()

    def has_element(self, elem: Any, key: Callable = lambda elem: elem) -> bool:
        for e in self._data:
            if key(e) == elem:
                return True
        return False

    @property
    def top(self) -> Any:
        return self._data[-1]

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0
