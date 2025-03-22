import board
import player

def display(board):
  '''
  Displays a board
  '''
  print()
  print(board)
  print()

def playGame(board, player1, player2):
  '''
  A game of Connect-4; player1 starts.
  '''
  # player 1 is *next* (i.e., first)
  currentPlayer, nextPlayer = player2, player1 

  # run the game
  print('Welcome to Connect Four!')

  # As long as the game isn't over:
  #   (1) display the current board
  #   (2) switch players
  #   (3) get a move from the current player
  #   (4) perform that move
  while not (board.isFull() or board.winsFor(currentPlayer.checker)):
    display(board)
    currentPlayer, nextPlayer = nextPlayer, currentPlayer
    move = currentPlayer.nextMove(board)
    board.dropChecker(move, currentPlayer.checker)
    print('{} drops in column {}...'.format(currentPlayer.checker, move))

  # print the final board and message
  display(board)
  if board.winsFor(currentPlayer.checker):
    print('{} wins -- Congratulations!'.format(currentPlayer.checker))
  else:
    print("Cat's game.")


def main():
  '''
  Play a game of Connect-4 between a human and the computer. Human goes first.
  '''
  game_board = board.Board()

  print("Select difficulty (0-5): ")

  while True:
    try:
      ply = int(input("Enter difficulty (0-5): "))
      if 0 <= ply <= 5:
        break
      else:
        print("Invalid input. Please enter a number between 0 and 5.")
    except ValueError:
      print("Invalid input.")
    
  print("\nSelect AI's tiebreaking strategy:")
  print("1: Always choose leftmost column")
  print("2: Always choose rightmost column")
  print("3: Choose a random column")

  while True:
    try:
      strategy = int(input("Enter a strategy (1-3): "))
      if strategy == 1:
        tiebreaker = player.LEFT
        break
      elif strategy == 2:
        tiebreaker = player.RIGHT
        break
      elif strategy == 3:
        tiebreaker = player.RANDOM
        break
      else:
        print("Please enter a valid strategy 1, 2, or 3.")
    except ValueError:
      print("Invalid Input.")

  first = input("\nWould you like to go first? (y/n): ").lower()

  human_player = player.HumanPlayer(board.X)
  computer = player.MachinePlayer(board.O, tiebreaker, ply)

  if first == 'y':
    playGame(game_board, human_player, computer)
  else:
    playGame(game_board, computer, human_player)

  play_again = input("Play again? (y/n): ").lower()

  if play_again == 'y':
    main()

if __name__ == '__main__':
  main()
