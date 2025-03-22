from board import X, O
import random


################################################################################
# Players
################################################################################
class Player:
    """
    A class that represents a Connect-4 Player.
    """

    def __init__(self, checker):
        self.checker = checker

    def nextMove(self, board):
        """
        Returns the column number into which the player wants to drop its checker.

        This naive player always drops its checker in the first column.
        """
        return 0


################################################################################
# Human Player
################################################################################
class HumanPlayer(Player):
    """
    A Player that can get the next move from the command line.
    """

    def nextMove(self, board):
        """
        Prompts the user to enter a move.

        Continues prompting until the move is valid.
        """
        while True:
            choice = input("{}'s choice: ".format(self.checker))
            try:
                column = int(choice)
                assert 0 <= column < board.numColumns(), "Not a valid column"
                assert not board.isColumnFull(column), "No room!"
            except ValueError:
                print("Invalid input: ", choice)
            except AssertionError as msg:
                print(msg)
            else:
                return column


################################################################################
# Tie Breakers
################################################################################
class TieBreaker:
    """
    A class whose instances act like functions. When an instance is called, it
    takes a list of scores, finds all the high scores, and breaks the tie to
    return the index (i.e., column number) of the winner.
    """

    def __init__(self, tiebreak):
        self._tiebreak = tiebreak

    def __call__(self, scores):
        """
        Find all the high scores in a list of scores and return the index of one of
        them, using the instance's tie-breaking strategy.
        """
        highScore = max(scores)
        allHighScores = [i for (i, s) in enumerate(scores) if s == highScore]
        return self._tiebreak(allHighScores)


LEFT = TieBreaker(lambda highest_scores: highest_scores[0])
RIGHT = TieBreaker(lambda highest_scores: highest_scores[-1])
RANDOM = TieBreaker(lambda highest_scores: random.choice(highest_scores))

################################################################################
# Machine Player
################################################################################

# Weights for winning, losing, and drawing
WIN = 100.0
LOSE = 0.0
DRAW = 50.0
FULL = -1


class MachinePlayer(Player):
    """
    A Player that uses strategies to "guess" the best move.
    """

    def __init__(self, checker, tiebreak, ply):
        Player.__init__(self, checker)
        self._tiebreak = tiebreak
        self._ply = ply

    def nextMove(self, board):
        return self.tiebreakMove(self.scoresFor(board))

    def otherChecker(self):
        """
        Returns the kind of checker that isn't mine.
        """
        if self.checker is X:
            return O
        else:
            return X

    def tiebreakMove(self, scores):
        """
        When many moves seem equally good, break the tie and return the column into
        which I should drop a checker.
        """
        return self._tiebreak(scores)

    def scoreOneBoard(self, board):
        if board.winsFor(self.checker):
            return WIN
        elif board.winsFor(self.otherChecker()):
            return LOSE
        return DRAW

    def isGameOver(self, board):
        if board.isFull():
            return True
        if board.winsFor(self.checker) or board.winsFor(self.otherChecker()):
            return True
        return False

    def scoresFor(self, board):
        scores = [0] * board.width

        for col in range(board.width):
            if board.isColumnFull(col):
                scores[col] = FULL
                continue

            if self.isGameOver(board) or (self._ply == 0):
                scores[col] = self.scoreOneBoard(board)
                continue

            board.dropChecker(col, self.checker)

            if self.isGameOver(board):
                scores[col] = self.scoreOneBoard(board)

            else:
                opponent = MachinePlayer(self.otherChecker(), self._tiebreak, self._ply - 1)
                opponent_scores = opponent.scoresFor(board)
                valid_scores = [score for score in opponent_scores if score != FULL]
            
                if not valid_scores:
                    scores[col] = DRAW
                
                else:
                    opponent_best_score = max(valid_scores)

                    if opponent_best_score == WIN:
                        scores[col] = LOSE

                    if opponent_best_score == LOSE:
                        scores[col] = WIN

                    else:
                        scores[col] = DRAW
        
            board.removeChecker(col)

        return scores
