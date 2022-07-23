import pickle

from enum import Enum
from typing import Any, Union, Tuple

MaybePiece = Union[int, None]
Row = Tuple[MaybePiece, MaybePiece, MaybePiece]
BoardState = Tuple[Row, Row, Row]

class Board:
    class Piece(Enum):
        O = 0
        X = 1

    def __init__(self) -> None:
        initial_state = [[None, None, None],
                         [None, None, None],
                         [None, None, None]]
        self.states = [pickle.dumps(initial_state)]

    def get_available_pieces():
        pass

    @property
    def state(self) -> BoardState:
        return pickle.loads(self.states[-1])

    def add_piece(self, position: Tuple[int, int], piece: Piece) -> None:
        x, y = position
        new_state = self.state
        new_state[x][y] = piece

        self._update_state(new_state)

    def is_position_valid(self, position: Tuple[int, int]) -> bool:
        x, y = position

        return x in range(3) and y in range(3)

    def is_position_empty(self, position: Tuple[int, int]) -> bool:
        x, y = position

        return self.state[x][y] is None

    def has_winning_state(self) -> bool:
        return (self._has_winning_vertical_state()
                or self._has_winning_horizontal_state()
                or self._has_winning_diagonal_state())

    def has_tie_state(self):
        return not (self.has_winning_state() or self._has_empty_position())

    def has_end_state(self):
        return self.has_winning_state() or self.has_tie_state()

    def get_available_positions(self):
        available_positions = []

        for row_idx, row in enumerate(self.state):
            for col_idx, piece in enumerate(row):
                if piece is None:
                    available_positions.append((row_idx, col_idx))

        return available_positions

    # Private methods

    def _has_winning_vertical_state(self) -> bool:
        current_state = self.state

        for col in range(3):
            if (current_state[0][col]
                    == current_state[1][col]
                    == current_state[2][col]
                    and current_state[0][col] is not None):
                return True

        return False

    def _has_winning_horizontal_state(self) -> bool:
        current_state = self.state

        for row in range(3):
            if (current_state[row][0]
                    == current_state[row][1]
                    == current_state[row][2]
                    and current_state[row][0] is not None):
                return True

        return False

    def _has_winning_diagonal_state(self) -> bool:
        current_state = self.state

        return ((current_state[0][0]
                 == current_state[1][1]
                 == current_state[2][2]
                 and current_state[1][1] is not None)
                or
                (current_state[0][2]
                 == current_state[1][1]
                 == current_state[2][0]
                 and current_state[1][1] is not None))

    def _update_state(self, state: Any) -> None:
        serialized_state = pickle.dumps(state)
        self.states.append(serialized_state)

    def _has_empty_position(self):
        for row in self.state:
            for position in row:
                if position is None:
                    return True

        return False
