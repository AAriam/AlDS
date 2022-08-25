from typing import Any, List, Tuple


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    @property
    def start_state(self) -> Any:
        """
        The start state of the search problem.
        """
        raise NotImplementedError

    def is_goal(self, state: Any) -> bool:
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
        raise NotImplementedError

    def successors(self, state: Any) -> List[Tuple]:
        """
          state: Search state

        Returns
        -------
        List[Tuple]
        A list of tuples, where each tuple is a triplet (state, action, action_cost), corresponding
        to a successor state; 'state' is the state of the successor, 'action' is the action
        required to get to that state from the parent state, and 'action_cost' is the cost  of
        expanding to the successor state from the parent state via the given action.
        """

        def actions(state) -> List[Any]:
            """
            Given a state, return a list of actions that can be executed in that state.
            """
            raise NotImplementedError

        def result(state, action) -> Any:
            """
            Given a state and an action executable in that state, return the resulting state.
            """
            raise NotImplementedError

        def cost(start_state, action, end_state) -> float:
            """
            Return the numeric cost of applying the `action` in `start_state` to reach `end_state`.
            """
            raise NotImplementedError

        avail_actions = actions(state)
        successors = []
        for action in avail_actions:
            end_state = result(state, action)
            successors.append((end_state, action, cost(state, action, end_state)))
        return successors

    def cost_actions(self, actions) -> float:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        raise NotImplementedError

    def heuristic(self, state) -> float:
        raise NotImplementedError
