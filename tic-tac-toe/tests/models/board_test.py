from tic_tac_toe.models.board import Board


def test_add_piece():
    board = Board()
    board.add_piece((0, 0), Board.PIECES.X)
    assert board.state == [[Board.PIECES.X, None, None],
                           [None, None, None],
                           [None, None, None]]
