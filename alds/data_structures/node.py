"""Module containing node structures."""

from __future__ import annotations
from typing import Any, Generator, Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class Node:
    """
    A Node in a search tree.

    Attributes
    ----------
    state : Any
        State of the node.
    action : Any
        The action required to get to the node's state from the parent node's state.
    parent : Node
        The parent node.
    path_cost : float
        The cost of the full path from root to this node. For the root node, this is equal to 0.
        For all other nodes created through the `expand` method, this will be automatically
        assigned as the sum of the parent node's `path_cost` and the cost of the `action` leading
        to this node from the parent node.
    """
    state: Any
    action: Any = None
    parent: Node = None
    path_cost: float = 0
    depth: int = 0

    def __repr__(self):
        return str(self.state)

    @property
    def path(self) -> np.ndarray[Any]:
        """
        The path to this node.

        Returns
        -------
        numpy.ndarray
            An array of actions that lead to this node, starting from the root node.
        """
        return self._path_finder_("action")

    @property
    def node_path(self) -> np.ndarray[Node]:
        """
        The tree-path to this node.

        Returns
        -------
        numpy.ndarray
            An array of `Node` objects that lead to this node, starting from the root node.
        """
        return self._path_finder_("node")

    def expand(self, successors_func: Callable) -> Generator[Node]:
        """
        Expand this node.

        Parameters
        ----------
        successors_func : Callable
            A function that takes a `state` as the only argument,  and returns a list of tuples,
            each corresponding to a successor state of the input state. Each tuple should contain
            three elements, corresponding to the state of the successor, the action required to get
            to that state, and the cost of that action.
        name_func : Callable (optional)
            A function that takes a `state` as the only argument,  and returns a string to be used
            as the node's name.

        Returns
        -------
        Generator[Node]
            A generator object containing the child nodes as `Node` objects.
        """
        for state, action, step_cost in successors_func(self.state):
            yield Node(
                state=state,
                action=action,
                parent=self,
                path_cost=step_cost + self.path_cost,
                depth=self.depth + 1
            )

    def _path_finder_(self, path_type):
        current_node = self
        path_length = self.depth + (1 if path_type == "node" else 0)
        path = np.empty(
            path_length,
            dtype=object if path_type == "node" else type(self.action)
        )
        if path_type == "node":
            for i in range(1, path_length+1):
                path[-i] = current_node
                current_node = current_node.parent
        elif path_type == "action":
            for i in range(path_length):
                path[-i] = current_node.action
                current_node = current_node.parent
        else:
            raise ValueError("`path_type` not recognized.")
        return path
