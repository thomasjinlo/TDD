from tic_tac_toe.models.player import Player

def test_prompt_move_accepts_user_input(mocker):
    player = Player()
    input_mock = mocker.patch("builtins.input", side_effect="0 0")
    assert player.prompt_move() == (0, 0)

    input_mock = mocker.patch("builtins.input", side_effect="1 1")
    assert player.prompt_move() == (1, 1)


# def test_prompt_move_accepts_arbitrary_spaces():
#     player = Player()
#     assert player.prompt_move() == (0, 0)
