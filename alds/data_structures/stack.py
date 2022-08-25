"""Module containing node structures."""

from typing import Any, Callable, Optional


class Stack:
    """
    A data structure with a last-in-first-out (LIFO) queuing policy.
    """

    def __init__(self, init_stack: Optional[list] = None):
        """
        Initialize a new stack, either empty or with an initial number of element.

        Parameters
        ----------
        init_stack : list, default: None
            An initial list of elements to add to the stack. Elements will be added to/popped from
            the end of the list.
        """
        if init_stack is None:
            self._data = []
        elif isinstance(init_stack, list):
            self._data = init_stack
        else:
            raise TypeError("Argument `init_stack` must be of type `list`.")
        return

    def __str__(self):
        return ", ".join([str(elem) for elem in self._data[-1::-1]])

    def push(self, element: Any) -> None:
        """Add a new element to the stack."""
        self._data.append(element)
        return

    def pop(self) -> Any:
        """Pop the most recently pushed element from the stack."""
        return self._data.pop()

    @property
    def top(self) -> Any:
        """Return the most recently pushed item from the stack, without removing."""
        return self._data[-1]

    @property
    def is_empty(self) -> bool:
        """Whether the stack is empty."""
        return len(self._data) == 0

    def has_element(self, elem: Any, key: Callable = lambda elem: elem) -> bool:
        """
        Whether a given element is present in the stack.

        Parameters
        ----------
        elem : Any
            The element to be checked.
        key : Callable, default: lambda elem: elem
            A function that inputs an element in the stack, and returns the value that must be
            checked against the argument `elem`.

        Returns
        -------
        bool
        """
        for e in self._data:
            if key(e) == elem:
                return True
        return False
