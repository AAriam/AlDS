"""Module containing queue data structures, such as FIFO, LIFO, and priority queues."""

from typing import Any, Callable, Optional, NoReturn
import heapq
from .abc import Queue


class FIFOQueue(Queue):
    """A queue data structure with a first-in-first-out (FIFO) policy."""

    def __init__(self, initial_queue: Optional[list[Any]] = None):
        if initial_queue is None:
            self._data = []
        elif isinstance(initial_queue, list):
            self._data = initial_queue.copy()
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

    def has_element(self, element: Any, key: Callable = lambda elem: elem) -> bool:
        for elem in self._data:
            if key(elem) == element:
                return True
        return False

    @property
    def top(self) -> Any:
        return self._data[-1]

    @property
    def is_empty(self):
        return len(self._data) == 0


class LIFOQueue(Queue):
    """A queue data structure with a last-in-first-out (LIFO) policy, also known as a stack."""

    def __init__(self, initial_queue: Optional[list[Any]] = None):
        if initial_queue is None:
            self._data = []
        elif isinstance(initial_queue, list):
            self._data = initial_queue.copy()
        else:
            raise TypeError("Argument `init_queue` must be of type `list`.")
        return

    def __str__(self):
        return ", ".join([str(elem) for elem in self._data[-1::-1]])

    def __repr__(self):
        return f"{type(self).__name__}({self._data})"

    def push(self, element: Any) -> NoReturn:
        self._data.append(element)
        return

    def pop(self) -> Any:
        return self._data.pop()

    def has_element(self, element: Any, key: Callable = lambda elem: elem) -> bool:
        for elem in self._data:
            if key(elem) == element:
                return True
        return False

    @property
    def top(self) -> Any:
        return self._data[-1]

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0


class PriorityQueue(Queue):
    """A queue data structure with a highest-priority-first-out (HPFO) policy, also known as a
    priority queue."""

    def __init__(self, initial_queue: Optional[list[tuple[Any, float]]] = None):
        self._counter = 0
        self._data = []
        if isinstance(initial_queue, list):
            for element, priority in initial_queue:
                self.push(element, priority)
        return

    def __str__(self):
        elems = [(e[2], (int(e[0]) if int(e[0])==e[0] else e[0])) for e in self._data]
        elems.sort(key=lambda e: e[1])
        return str(elems)

    def push(self, element: Any, priority: float = 0) -> NoReturn:
        entry = (priority, self._counter, element)
        heapq.heappush(self._data, entry)
        self._counter += 1
        return

    def pop(self, return_priority: bool = False) -> Any:
        priority, counter, element = heapq.heappop(self._data)
        if return_priority:
            return element, priority
        return element

    def has_element(self, element: Any, key: Callable = lambda elem: elem) -> bool:
        for priority, counter, elem in self._data:
            if key(elem) == element:
                return True
        return False

    def update(self, element: Any, priority: float):
        """Update the queue with a given element.
        If the element is already in priority queue with a higher priority, update its priority
        and rebuild the heap. If the element in the queue has an equal or lower priority,
        do nothing. Otherwise, if element is not in the queue, push the element into the queue.
        """
        for index, (prio, count, elem) in enumerate(self._data):
            if elem == element:
                if prio <= priority:
                    break
                del self._data[index]
                self._data.append((priority, count, element))
                heapq.heapify(self._data)
                break
        else:
            self.push(element, priority)

    @property
    def top(self, return_priority: bool = False) -> Any:
        raise NotImplementedError

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0