"""Module containing node structures."""

from typing import Any, Callable


class Stack:
    """
    A data container with a last-in-first-out (LIFO) queuing policy.

    Methods
    -------
    push
        Push a new object into the stack.

    pop
        Remove the last pushed object from the stack and return it.

    Attributes
    ----------
    is_empty : bool
        Whether the stack is empty or not.
    """
    def __init__(self, init_stack: list = None):
        """
        Initialize a new stack, either empty or with some initial objects.

        Parameters
        ----------
        init_stack : List (optional; default: None)
            An initial list of objects to add to the stack. Objects will be added to/popped from
            the end of the list.
        """
        if init_stack is None:
            self._data = []
        elif type(init_stack) is list:
            self._data = init_stack
        else:
            raise TypeError("Type of `init_stack` should be `list`.")
        return

    def __str__(self):
        copy = self._data.copy()
        copy.reverse()
        return str(copy)

    def push(self, obj: Any) -> None:
        """Add a new element to the stack."""
        self._data.append(obj)
        return

    def pop(self) -> Any:
        """Pop the most recently pushed item from the stack."""
        return self._data.pop()

    @property
    def top(self) -> Any:
        """Return the most recently pushed item from the stack, without removing."""
        return self._data[-1]

    @property
    def is_empty(self) -> bool:
        """Whether the stack is empty or not."""
        return len(self._data) == 0

    def has_element(self, elem: Any, key: Callable = lambda elem: elem) -> bool:
        for e in self._data:
            if key(e) == elem:
                return True
        return False
