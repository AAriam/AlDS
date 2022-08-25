"""Module containing node structures."""

from __future__ import annotations
from collections.abc import Iterator
from typing import Any
from dataclasses import dataclass
from alds.search.abc import SearchProblem


@dataclass(frozen=True, slots=True)
class Node:
    """
    A Node in a search tree.

    Attributes
    ----------
    state : Any
        State of the node.
    action : Any, default: None
        The action required to get to the node's state from the parent node's state.
    parent : Node, default: None
        The parent node.
    path_cost : float, default: 0
        The cost of the full path from root to this node. For the root node, this is equal to 0.
        For all other nodes created through the `expand` method, this will be automatically
        assigned as the sum of the parent node's `path_cost` and the cost of the `action` leading
        to this node from the parent node.
    depth : int, default: 0
        Depth of the node in the tree. For the root node, this is equal to 0.
        For all other nodes created through the `expand` method, this will be automatically
        assigned as the depth of the parent node plus 1.
    """

    state: Any
    action: Any = None
    parent: Node = None
    path_cost: float = 0
    depth: int = 0

    def __str__(self):
        return str(self.state)

    @property
    def path_actions(self) -> list[Any]:
        """
        The path to this node.

        Returns
        -------
        numpy.ndarray
            An array of actions that lead to this node, starting from the root node.
        """
        path = []
        current_node = self
        while current_node.parent is not None:
            path.insert(0, current_node.action)
            current_node = current_node.parent
        return path

    @property
    def path_states(self) -> list[Any]:
        """
        The tree-path to this node.

        Returns
        -------
        numpy.ndarray
            An array of `Node` objects that lead to this node, starting from the root node.
        """
        path = []
        current_node = self
        while current_node.parent is not None:
            path.insert(0, current_node.state)
            current_node = current_node.parent
        path.insert(0, current_node.parent)
        return path

    def expand(self, search_problem: SearchProblem) -> Iterator[Node]:
        """
        Expand this node.

        Parameters
        ----------
        search_problem : SearchProblem
            A search problem with a `successors` method
            as described in `alds.search.abc.SearchProblem`.

        Returns
        -------
        Iterator[Node]
            An iterator containing the child nodes as `Node` objects.
        """
        for action, successor_state, action_cost in search_problem.successors(self.state):
            yield Node(
                state=successor_state,
                action=action,
                parent=self,
                path_cost=action_cost + self.path_cost,
                depth=self.depth + 1
            )
