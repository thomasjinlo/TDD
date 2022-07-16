import pickle

from enum import Enum
from typing import Any, Union

MaybePiece = Union[int, None]
Row = list[MaybePiece, MaybePiece, MaybePiece]
BoardState = list[Row, Row, Row]

class Board:
    class Piece(Enum):
        O = 0
        X = 1

    def __init__(self) -> None:
        initial_state = [[None, None, None],
                         [None, None, None],
                         [None, None, None]]
        self.states = [pickle.dumps(initial_state)]

    @property
    def state(self) -> BoardState:
        return pickle.loads(self.states[-1])

    def add_piece(self, position: tuple[int, int], piece: Piece) -> None:
        x, y = position
        new_state = self.state
        new_state[x][y] = piece

        self._update_state(new_state)

    def is_position_valid(self, position: tuple[int, int]) -> bool:
        x, y = position

        return x in range(3) and y in range(3)

    def is_position_empty(self, position: tuple[int, int]) -> bool:
        x, y = position

        return self.state[x][y] is None

    def has_winning_state(self) -> bool:
        return (self._has_winning_vertical_state()
                or self._has_winning_horizontal_state()
                or self._has_winning_diagonal_state())

    def _has_winning_vertical_state(self) -> bool:
        current_state = self.state

        for col in range(3):
            if (current_state[0][col]
                    == current_state[1][col]
                    == current_state[2][col]):
                return True

        return False

    def _has_winning_horizontal_state(self) -> bool:
        current_state = self.state

        for row in range(3):
            if (current_state[row][0]
                    == current_state[row][1]
                    == current_state[row][2]):
                return True

        return False

    def _has_winning_diagonal_state(self) -> bool:
        current_state = self.state

        return ((current_state[0][0]
                 == current_state[1][1]
                 == current_state[2][2])
                or
                (current_state[0][2]
                 == current_state[1][1]
                 == current_state[2][0]))

    def _update_state(self, state: Any) -> None:
        serialized_state = pickle.dumps(state)
        self.states.append(serialized_state)
