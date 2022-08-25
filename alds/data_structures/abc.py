from abc import ABC, abstractmethod
from typing import Any, Callable, NoReturn, Optional


class Queue(ABC):

    @abstractmethod
    def __init__(self, initial_queue: Optional[list] = None):
        """
        Initialize a new queue, either empty or with an initial number of elements.

        Parameters
        ----------
        initial_queue : list, default: None
           An initial list of elements to add to the queue. The list should be ordered in such a
           way that the top element in the queue is the last element in the list.
        """
        ...

    @abstractmethod
    def push(self, element: Any) -> NoReturn:
        """Add a new element to the queue."""
        ...

    @abstractmethod
    def pop(self) -> Any:
        """Pop (remove and return) the top element from the queue, according to its policy."""
        ...

    @abstractmethod
    def top(self) -> Any:
        """Return the top element from the queue (without removing), according to its policy."""
        ...

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """Whether the queue is empty."""
        ...

    @abstractmethod
    def has_element(self, element: Any, key: Callable = lambda elem: elem) -> bool:
        """
        Whether a given element is present in the queue.

        Parameters
        ----------
        element : Any
            The element to be checked.
        key : Callable, default: lambda elem: elem
            A function that inputs an element from the queue, and returns the value that must be
            checked against the argument `element`.

        Returns
        -------
        bool
        """