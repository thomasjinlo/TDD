import pytest

from tic_tac_toe.models.board import Board


@pytest.fixture
def board():
    return Board()

def test_add_piece(board):
    board.add_piece((0, 0), Board.Piece.X)
    assert board.state == [[Board.Piece.X, None, None],
                           [None, None, None],
                           [None, None, None]]


def test_position_is_valid(board):
    assert board.is_position_valid((0, 0))
    assert board.is_position_valid((0, 1))
    assert board.is_position_valid((0, 2))
    assert board.is_position_valid((1, 0))
    assert board.is_position_valid((1, 1))
    assert board.is_position_valid((1, 2))
    assert board.is_position_valid((2, 0))
    assert board.is_position_valid((2, 1))
    assert board.is_position_valid((2, 2))


def test_position_is_not_valid(board):
    assert board.is_position_valid((-1, 0)) is False
    assert board.is_position_valid((3, 0)) is False
    assert board.is_position_valid((0, -1)) is False
    assert board.is_position_valid((0, 3)) is False
    assert board.is_position_valid((-1, -1)) is False
    assert board.is_position_valid((-1, 3)) is False
    assert board.is_position_valid((3, 3)) is False
    assert board.is_position_valid((3, -1)) is False


def test_position_is_empty(board):
    assert board.is_position_empty((0, 0))


def test_position_is_not_empty(board):
    board.add_piece((0, 0), Board.Piece.X)
    assert board.is_position_empty((0, 0)) is False


def test_has_no_winning_state(board):
    board.add_piece((0, 0), Board.Piece.X)
    board.add_piece((1, 1), Board.Piece.X)
    board.add_piece((2, 2), Board.Piece.O)
    assert board.has_winning_state() is False


def test_has_winning_state_vertically(board):
    board.add_piece((0, 0), Board.Piece.O)
    board.add_piece((1, 0), Board.Piece.O)
    board.add_piece((2, 0), Board.Piece.O)
    assert board.has_winning_state()


def test_has_winning_state_horizontally(board):
    board.add_piece((0, 0), Board.Piece.O)
    board.add_piece((0, 1), Board.Piece.O)
    board.add_piece((0, 2), Board.Piece.O)
    assert board.has_winning_state()


def test_has_winning_state_diagonally():
    board = Board()
    board.add_piece((0, 0), Board.Piece.O)
    board.add_piece((1, 1), Board.Piece.O)
    board.add_piece((2, 2), Board.Piece.O)
    assert board.has_winning_state()
    board = Board()
    board.add_piece((0, 2), Board.Piece.O)
    board.add_piece((1, 1), Board.Piece.O)
    board.add_piece((2, 0), Board.Piece.O)
    assert board.has_winning_state()


def test_has_no_cats_game_and_winning_state():
    board = Board()
    board.add_piece((0, 0), Board.Piece.O)
    board.add_piece((0, 1), Board.Piece.O)
    board.add_piece((1, 2), Board.Piece.O)
    board.add_piece((2, 0), Board.Piece.O)
    board.add_piece((2, 2), Board.Piece.O)
    board.add_piece((1, 0), Board.Piece.X)
    board.add_piece((1, 1), Board.Piece.X)
    board.add_piece((2, 1), Board.Piece.X)

    assert board.has_winning_state() is False
    assert board.has_cats_game() is False


def test_has_cats_game():
    board = Board()
    board.add_piece((0, 0), Board.Piece.O)
    board.add_piece((0, 1), Board.Piece.O)
    board.add_piece((1, 2), Board.Piece.O)
    board.add_piece((2, 0), Board.Piece.O)
    board.add_piece((2, 2), Board.Piece.O)
    board.add_piece((0, 2), Board.Piece.X)
    board.add_piece((1, 0), Board.Piece.X)
    board.add_piece((1, 1), Board.Piece.X)
    board.add_piece((2, 1), Board.Piece.X)

    assert board.has_winning_state() is False
    assert board.has_cats_game()
