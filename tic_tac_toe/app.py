from typing import Optional



class Game:
    def __init__(self):
        self.current_player = 'X'
        self.is_over = False
        self.winner = Optional[str]
        self.grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    def check_column_win(self) -> bool:
        for col in range(3):
            if (self.grid[0][col] ==
                self.grid[1][col] ==
                self.grid[2][col] != ' '):
                self.winner = self.grid[0][col]
                return True
        return False

    def check_row_win(self) -> bool:
        for row in range(3):
            if (self.grid[row][0] ==
                self.grid[row][1] ==
                self.grid[row][2] != ' '):
                self.winner = self.grid[row][0]
                return True
        return False

    def check_diagonal_win(self) -> bool:
        if (self.grid[0][0] ==
            self.grid[1][1] ==
            self.grid[2][2] != ' '):
            self.winner = self.grid[0][0]
            return True

        if (self.grid[0][2] ==
            self.grid[1][1] ==
            self.grid[2][0] != ' '):
            self.winner = self.grid[0][2]
            return True
        return False

    def match_null_state(self) -> bool:
        return all(
            cell != ' '
            for row in self.grid
            for cell in row
        )
    # Evaluate game state after a move (win or draw)
    def evaluate_game_state(self):
        if (self.check_row_win() or
                self.check_column_win() or
                self.check_diagonal_win()):
            self.is_over = True
            return
        is_grid_full = self.match_null_state()
        if is_grid_full and self.winner is None:
            print("No winner!")
            self.is_over = True
            return

    def play(self, move: str):
        # Validate input format
        if len(move) != 2:
            raise ValueError("Invalid move format. Use format 'A1', 'B2', etc.")
        col_move = move[0]

        # Validate row
        if int(move[1]) not in (1, 2, 3):
            raise ValueError(f"Invalid row '{move[1]}'. Choose 1, 2, or 3.")
        row_index = int(move[1]) - 1
        col_object = {"A": 0, "B": 1, "C": 2}

        # Validate column
        if col_move not in col_object.keys():
            raise ValueError(f"Invalid column '{col_move}'. Choose from A, B, or C.")
        col_index = col_object[col_move]

        # Check if cell is free
        if self.grid[row_index][col_index] != ' ':
            raise ValueError(f"Cell {move} is already taken.")
        else:
            self.grid[row_index][col_index] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        self.evaluate_game_state()


