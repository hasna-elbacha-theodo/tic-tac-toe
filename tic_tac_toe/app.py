from typing import Optional



class Game:
    winner: Optional[str]
    current_player = 'X'
    is_over = False
    grid: list[list[str]] = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    #Rules
#there are two players in the game (X and O)
# a game has nine fields in a 3x3 grid
#players take turns taking fields until the game is over
#a player can take a field if not already taken
#a game is over when all fields in a row are taken by a player
#a game is over when all fields in a column are taken by a player
#a game is over when all fields in a diagonal are taken by a player
#a game is over when all fields are taken
    def check_winner(self):
        self.winner = None
        win_lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],

            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for line in win_lines:
            values = [self.grid[r][c] for r, c in line]

            if values == ["X", "X", "X"]:
                self.winner = "X"
                self.is_over = True
                return
            if values == ["O", "O", "O"]:
                self.winner = "O"
                self.is_over = True
                return
            full = all(cell != " " for row in self.grid for cell in row)
            if full and self.winner is None:
                print("No winner!")
                self.is_over = True
                return

    def play(self, move: str):
       col_move = move[0]
       row_index= int(move[1])
       col_object = {"A": 0, "B": 1, "C": 2}
       col_index = col_object[col_move]
       if self.grid[row_index][col_index]== " ":
                      self.grid[row_index][col_index] = self.current_player
                      if self.current_player == 'X':
                          self.current_player = 'O'
                      else:
                          self.current_player = 'X'
       self.check_winner()


