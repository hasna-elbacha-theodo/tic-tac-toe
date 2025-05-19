import pytest
from tic_tac_toe.app import Game


def test_valid_move_switch_player():
    game = Game()
    game.play('A1')
    assert game.grid[0][0] == 'X'
    assert game.current_player == 'O'


def test_invalid_format_length():
    game = Game()
    with pytest.raises(ValueError, match=r"Invalid move format.*"):
        game.play('A11')

def test_invalid_row():
    game = Game()
    with pytest.raises(ValueError, match=r"Invalid row '4'.*"):
        game.play('A4')

def test_invalid_column():
    game = Game()
    with pytest.raises(ValueError, match=r"Invalid column 'Z'.*"):
        game.play('Z1')

def test_cell_already_taken():
    game = Game()
    game.play('A2')
    with pytest.raises(ValueError) as excinfo:
        game.play('A2')
    assert "Cell A2 is already taken." in str(excinfo.value)
def test_if_column_wins():
    game = Game()
    game.play('A1')#X
    game.play('B2')#O
    game.play('A2')#X
    game.play('B1')#O
    game.play('A3')#X
    assert game.check_column_win() is True
    assert game.winner=="X"

def test_if_row_wins():
    game = Game()
    game.play('A1')#X
    game.play('A2')#O
    game.play('B1')#X
    game.play('B2')#O
    game.play('C1')#X
    assert game.check_row_win() is True
    assert game.winner=="X"

def test_if_diagonal_wins():
    game = Game()
    game.play('A1')#X
    game.play('A2')#O
    game.play('B2')#X
    game.play('B1')#O
    game.play('C3')#X
    assert game.check_diagonal_win() is True
    assert game.winner=="X"

def test_if_game_over():
    game = Game()
    game.play('A1')  # X
    game.play('A2')  # O
    game.play('B2')  # X
    game.play('B1')  # O
    game.play('C3')  # X
    assert game.is_over is True

def test_match_null():
    game = Game()
    game.play('A1')
    game.play('B2')
    game.play('B1')
    game.play('C1')
    game.play('A3')
    game.play('A2')
    game.play('C2')
    game.play('B3')
    game.play('C3')
    assert game.match_null_state() is True
