from tic_tac_toe.tic_tac_toe import TicTacToe
from tic_tac_toe.models.board import Board
from tic_tac_toe.models.player import Player


def test_tic_tac_toe_selects_user_piece(mocker):
    board = Board()
    tic_tac_toe = TicTacToe(board)

    select_piece_mock = mocker.patch.object(tic_tac_toe, "select_piece")
    
    tic_tac_toe.initialize_game()
    
    select_piece_mock.assert_called_once()


# def test_select_piece_gets_available_pieces(mocker):
#     board = Board()
#     tic_tac_toe = TicTacToe(board)
# 
#     mocker.patch.object(board, "get_available_pieces")
# 
#     tic_tac_toe.select_piece()
# 
#     board.get_available_pieces.assert_called_once()


def test_select_piece_prompts_message(mocker, capfd):
    board = Board()
    tic_tac_toe = TicTacToe(board)

    available_pieces = ["piece1", "piece2"]
    mocker.patch.object(board, "get_available_pieces", return_value=available_pieces)
    mocker.patch.object(tic_tac_toe, "get_piece_message")
    mocker.patch("builtins.input", side_effect=["piece1"])

    tic_tac_toe.select_piece()

    tic_tac_toe.get_piece_message.assert_called_once_with(available_pieces)


def test_selects_valid_piece(mocker, capfd):
    board = Board()
    tic_tac_toe = TicTacToe(board)

    valid_piece = "piece1"
    available_pieces = [valid_piece, "piece2"]
    mocker.patch.object(board, "get_available_pieces", return_value=available_pieces)
    mocker.patch.object(tic_tac_toe, "get_piece_message")
    mocker.patch("builtins.input", side_effect=[valid_piece])

    tic_tac_toe.select_piece()

    valid_piece_message, err = capfd.readouterr()

    assert valid_piece_message == f'Player 1 selected piece: {valid_piece}.\n'


def test_prompts_user_until_valid_piece(mocker, capfd):
    board = Board()
    tic_tac_toe = TicTacToe(board)

    invalid_piece = "piece3"
    valid_piece = "piece1"
    available_pieces = [valid_piece, "piece2"]
    mocker.patch.object(board, "get_available_pieces", return_value=available_pieces)
    mocker.patch.object(tic_tac_toe, "get_piece_message")
    mocker.patch("builtins.input", side_effect=[invalid_piece, valid_piece])

    tic_tac_toe.select_piece()

    all_messages, err = capfd.readouterr()
    invalid_message, valid_message = all_messages.split("\n", 1)

    assert invalid_message == f'Invalid piece selected: {invalid_piece}. Try again'
    assert valid_message == f'Player 1 selected piece: {valid_piece}.\n'


def test_get_piece_message(mocker):
    board = Board()
    tic_tac_toe = TicTacToe(board)

    available_pieces = ["piece1", "piece2"]
    message = tic_tac_toe.get_piece_message(available_pieces)

    assert message == "Please enter a piece from options [piece1, piece2]: "


def test_tic_tac_toe_player1_wins(mocker):
    board = Board()
    tic_tac_toe = TicTacToe(board)


    print_winner_mock = mocker.patch.object(tic_tac_toe, "print_winner")

    prompt_1_mock = mocker.patch.object(player1, "prompt_move")
    prompt_2_mock = mocker.patch.object(player2, "prompt_move")

    prompt_1_mock.side_effect = [(0, 0), (0, 1), (0, 2)]
    prompt_2_mock.side_effect = [(1, 0), (1, 1), (1, 2)]

    tic_tac_toe.start_game()

    print_winner_mock.assert_called_once_with(player1)


# def test_tic_tac_toe_player2_wins(mocker):
#     board = Board()
#     player1 = Player()
#     player2 = Player()
#     tic_tac_toe = TicTacToe(board, player1, player2)
# 
#     mocker.patch.object(player1, "piece", Board.Piece.X)
#     mocker.patch.object(player2, "piece", Board.Piece.O)
#     print_winner_mock = mocker.patch.object(tic_tac_toe, "print_winner")
# 
#     prompt_1_mock = mocker.patch.object(player1, "prompt_move")
#     prompt_2_mock = mocker.patch.object(player2, "prompt_move")
# 
#     prompt_1_mock.side_effect = [(0, 0), (0, 1), (2, 2)]
#     prompt_2_mock.side_effect = [(1, 0), (1, 1), (1, 2)]
# 
#     tic_tac_toe.start_game()
# 
#     print_winner_mock.assert_called_once_with(player2)
# 
# 
# def test_tic_tac_toe_tie_game(mocker):
#     board = Board()
#     player1 = Player()
#     player2 = Player()
#     tic_tac_toe = TicTacToe(board, player1, player2)
# 
#     mocker.patch.object(player1, "piece", Board.Piece.X)
#     mocker.patch.object(player2, "piece", Board.Piece.O)
#     print_winner_mock = mocker.patch.object(tic_tac_toe, "print_winner")
#     print_tie_mock = mocker.patch.object(tic_tac_toe, "print_tie")
# 
#     prompt_1_mock = mocker.patch.object(player1, "prompt_move")
#     prompt_2_mock = mocker.patch.object(player2, "prompt_move")
# 
#     prompt_1_mock.side_effect = [(0, 0), (0, 1), (1, 2), (2, 0), (2, 2)]
#     prompt_2_mock.side_effect = [(1, 0), (1, 1), (0, 2), (2, 1)]
# 
#     tic_tac_toe.start_game()
# 
#     print_winner_mock.assert_not_called()
#     print_tie_mock.assert_called_once()
