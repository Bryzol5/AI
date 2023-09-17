from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player


class TicTacToe(TwoPlayerGame):
 def __init__(self, players):
  # Define the players
  self.players = players
  self.board = [0 for i in range(9)]
  self.current_player = 1
 # Define possible moves
 def possible_moves(self):
  return [i + 1 for i, e in enumerate(self.board) if e == 0]
 #  Make a move method
 def make_move(self, move):
  self.board[int(move) - 1] = self.current_player
 # Undo a move method (for bot)
 def unmake_move(self, move):
  self.board[int(move) - 1] = 0
 # Does the opponent have three in a line?
 def lose(self):
  return any(
   [
    all([(self.board[c - 1] == self.opponent_index) for c in
line])
    for line in [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 4, 7],
     [2, 5, 8],
     [3, 6, 9],
     [1, 5, 9],
     [3, 5, 7],
    ]
   ]
  )
 # Check if the game is over
 def is_over(self):
  return (self.possible_moves() == []) or self.lose()
 # Show board
 def show(self):
  print(
   "\n"
   + "\n".join(
    [
     " ".join([[".", "O", "X"][self.board[3 * j + i]] for i
in range(3)])
     for j in range(3)
    ]
   )
  )
 # Compute the score
 def scoring(self):
  return -100 if self.lose() else 0

if __name__ == "__main__":
 from easyAI import AI_Player, Negamax
 #Define the algorithm
 ai_algo = Negamax(6)
 #Start the game
 TicTacToe([Human_Player(), AI_Player(ai_algo)]).play()
