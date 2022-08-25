"""Module containing all abstract base classes for search algorithms."""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import Any


class SearchProblem(ABC):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    @property
    @abstractmethod
    def init_state(self) -> Any:
        """The initial state of the search problem."""
        ...

    @abstractmethod
    def is_goal_state(self, state: Any) -> bool:
        """
        Whether a given state is a goal state.

        Parameters
        ----------
        state : Any
            State to be checked.

        Returns
        -------
        bool
            True if the state is a valid goal state, otherwise False.
        """
        ...

    @abstractmethod
    def actions(self, state: Any) -> Iterable[Any]:
        """
        Given a state, return a list of actions that can be executed in that state.
        """
        ...

    @abstractmethod
    def result(self, state: Any, action: Any) -> Any:
        """
        Given a state and an action executable in that state, return the resulting state.
        """
        ...

    @abstractmethod
    def cost_action(self, start_state, action, end_state) -> float:
        """
        Return the numeric cost of applying the `action` in `start_state` to reach `end_state`.
        """
        ...

    def successors(self, state: Any) -> Iterator[tuple]:
        """
        Get all successor states of a given state, along their corresponding actions and cost.

        Parameters
        ----------
        state : Any
            State for which successors are to be generated.

        Returns
        -------
        Iterator[tuple]
            Each tuple is a triplet (state, action, action_cost), corresponding
            to a successor state; 'state' is the state of the successor, 'action' is the action
            required to get to that state from the parent state, and 'action_cost' is the cost of
            expanding to the successor state from the parent state via the given action.
        """
        for action in self.actions(state=state):
            successor_state = self.result(state=state, action=action)
            cost = self.cost_action(start_state=state, action=action, end_state=successor_state)
            yield action, successor_state, cost
        return

    def heuristic(self, state: Any) -> float:
        """
        Calculate the heuristic value of a given state.

        Parameters
        ----------
        state : Any
            State for which the heuristic value should be calculated.

        Returns
        -------
        float
            The heuristic value of the given state.
        """
        return 0
