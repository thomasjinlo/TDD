from tic_tac_toe.models.board import Board

class TicTacToe:

    def __init__(self, board):
        self.board = board
        self.current_piece = Board.Piece.X

    def start_game(self):
        while not self.board.has_end_state():
            self.board.add_piece(self.get_position(), self.current_piece)
            self.print_board()
            self.swap_piece()

        if self.board.has_winning_state():
            self.swap_piece()
            print(f'Player with piece {self.current_piece} won')
        else:
            print('Tie game')

    def print_board(self):
        for row in self.board.state:
            print(f'{row!r}')

    def get_position(self):
        available_positions = self.board.get_available_positions()
        str_position = input(f'Available positions {available_positions!r}\nPlease enter position: ')
        position = tuple(map(int, str_position.split(", ")))

        while position not in available_positions:
            str_position = input(f'Available positions {available_positions!r}\nPlease enter position: ')
            position = tuple(map(int, str_position.split(", ")))

        return position

    def swap_piece(self):
        if self.current_piece is Board.Piece.X:
            self.current_piece = Board.Piece.O
        else:
            self.current_piece = Board.Piece.X
