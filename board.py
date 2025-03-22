################################################################################
# Configuration
###############################################################################
DEFAULT_WIDTH  = 7
DEFAULT_HEIGHT = 6
WINNING_COUNT  = 4

################################################################################
# Checker
################################################################################
Checker = str     # an easy way to represent a Checker :)

X = Checker('X')
O = Checker('O')
BLANK = Checker(' ')

################################################################################
# Board
################################################################################
class Board:
  '''
  Represents a Connect-4 board.
  '''

  def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    self.width = width
    self.height = height
    self.board = [[BLANK for _ in range(width)] for _ in range(height)]

  def __str__(self):
    result = ""
    for row in self.board:
        # if row is something like ['X', 'O', 'X'], then "|".join(row) produces "X|O|X"
        result += "|" + "|".join(row) + "|\n"
    result += "-" * (self.width * 2 + 1) + "\n"
    result += " " + " ".join(str(i) for i in range(self.width)) + " \n"
    return result

  def numColumns(self):
    return self.width

  def numRows(self):
    return self.height

  def setCell(self, coord, checker):
    col, row = coord
    if col < 0 or col >= self.width or row < 0 or row >= self.height:
      raise ValueError("Invalid coordinates")
    self.board[row][col] = checker

  def getCell(self, coord):
    col, row = coord
    if col < 0 or col >= self.width or row < 0 or row >= self.height:
      raise ValueError("Invalid coordinates")
    return self.board[row][col]

  def column(self, n):
    if n < 0 or n >= self.width:
      raise ValueError("Invalid column")
    result = []
    for i in range(self.height):
      result.append(self.board[i][n])
    return result

  def row(self, n):
    if n < 0 or n >= self.height:
      raise ValueError("Invalid coordinates")
    result = []
    for i in range(self.width):
      result.append(self.board[n][i])
    return result

  def columns(self):
    result = []
    for col in range(self.width):
      for row in range(self.height):
        result.append(self.board[row][col])
    return result

  def rows(self):
    result = []
    for row in range(self.height):
      for col in range(self.width):
        result.append(self.board[row][col])
    return result

  def isColumnEmpty(self, col):
    if col < 0 or col >= self.width:
      raise ValueError("Invalid column")
    for row in range(self.height):
      if self.board[row][col] != BLANK:
        return False
    return True

  def isColumnFull(self, col):
    if col < 0 or col >= self.width:
      raise ValueError("Invalid column")
    for row in range(self.height):
      if self.board[row][col] == BLANK:
        return False
    return True
  
  def isFull(self):
    for row in range(self.height):
      for col in range(self.width):
        if self.board[row][col] == BLANK:
          return False
    return True

  def dropChecker(self, col, checker):
    if col < 0 or col >= self.width:
      raise ValueError("Invalid column")
    if self.isColumnFull(col):
      raise ValueError("Column is full")
    for row in range(self.height-1, -1, -1):
      if self.board[row][col] == BLANK:
        self.board[row][col] = checker
        return

  def removeChecker(self, col):
    if col < 0 or col >= self.width:
      raise ValueError("Invalid column")
    if self.isColumnEmpty(col):
      raise ValueError("Column is empty")
    for row in range(self.height):
      if self.board[row][col] != BLANK:
        self.board[row][col] = BLANK
        return

  def winsFor(self, checker):

    # Horizontal wins
    for row in range(self.height):
      for col in range(self.width - WINNING_COUNT + 1):
        if all(self.board[row][col+i] == checker for i in range(WINNING_COUNT)):
          return True
        
    # Vertical wins
    for col in range(self.width):
      for row in range(self.height - WINNING_COUNT + 1):
        if all(self.board[row+i][col] == checker for i in range(WINNING_COUNT)):
          return True
        
    # Diagonal wins (upward left to right)
    for row in range(WINNING_COUNT - 1, self.height):
      for col in range(self.width - WINNING_COUNT + 1):
        if all(self.board[row-i][col+i] == checker for i in range(WINNING_COUNT)):
          return True
                      
    # Diagonal wins (downward left to right)
    for row in range(self.height - WINNING_COUNT + 1):
      for col in range(self.width - WINNING_COUNT + 1):
        if all(self.board[row+i][col+i] == checker for i in range(WINNING_COUNT)):
          return True
                     
    return False

  def setBoard(self, moveString, startChecker=X):
    ''' 
    Accepts a string of column numbers and places alternating checkers in those 
    columns, starting with X.
    
    For example, call b.setBoard('012345') to see Xs and Os alternate on the
    bottom row, or b.setBoard('000000') to see them alternate in the left 
    column.

    moveString must be a string of integers.
    '''
    currentChecker = startChecker
    nextChecker = O if startChecker is X else X
    for colDigit in moveString:
      col = int(colDigit)
      self.dropChecker(col, currentChecker)
      currentChecker, nextChecker = nextChecker, currentChecker
