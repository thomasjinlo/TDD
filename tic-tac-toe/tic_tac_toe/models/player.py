import inspect

class Player:

    def __init__(self):
        self.piece = None

    def prompt_piece(self):
        pass

    def choose_opposite_piece(self, opposite_player):
        pass

    def prompt_move(self):
        move = input(self.move_prompt)
        return (0, 0)

    @property
    def move_prompt(self):
        prompt = """Enter row and column positions ranging from 0-2 separated by a space.
                    For example, '0 0' represents top left corner: """
        return inspect.cleandoc(prompt)
