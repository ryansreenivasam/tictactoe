from django.db import models

# This model holds information about the current game.  The board is a string 
# with a length of 9, allowing 1 letter for each of the 9 spaces on the board.
# The board begins as a string with 9 blank spaces.  The response field 
# determines if an AI move has been requested. Response will be set to True 
# after a new user move has been received. The winner field contains the 
# character of the winning player after they have won.  This will default to 
# 0 if a winner has not been declared.

class Game(models.Model):
    board = models.CharField(max_length=9, default=" " * 9)
    response = models.BooleanField(default=False)
    winner = models.CharField(max_length=1, default="0")

    # This specifies what to print when this model is printed
    def __str__(self):
        # Prints contents of board field
        return self.board


    # This method converts the board string into a list then passes that list 
    # to the minimax function to calculate the next move.
    def AIMove(self):
        # Split board string into list for further manipulation.
        boardList = list(self.board) 
        
         # Pass current board and O for AI player to find the next AI move.
        score, nextMove = self.minimax(boardList, "O")

        # Set the index of the AI's next move to O
        boardList[nextMove] = "O"

        # Check to see if the last AI move won the game
        if self.checkWinner(boardList) == "O":
            self.winner = "O"

        # Join indices of boardList into string and assign to board field.
        self.board = "".join(boardList)

        # We have generated a new move so a response is no longer needed
        self.response = False 


    # This method will determine the next move that the AI will make.  The
    # move is determined by using the minimax algorithm to recursively look 
    # through all possible future moves and choose the move that will win.
    # currBoard is the relevant board in list form.  player is the current 
    # player that is taking a turn.  player will either be O for AI or X
    # for user.  When minimax() is first called by AIMove, O is passed in 
    # so that a move for the AI is produced at the end of the process.

    def minimax(self, currBoard, player):
        # Start with a move that is not possible.
        bestMove = -1

        # First check for a winner of the current scenario
        winPlayer = self.checkWinner(currBoard)
        if winPlayer == player:
            # If the current player has won the game, return 1 to indicate that
            # this scenario is favorable to the current player.
            return 1, bestMove
        elif winPlayer == self.getOpponent(player):
            # If the opponent of the current player has won the game, return -1
            # to indicate that this scenario is favorable to the opponent.
            return -1, bestMove

        # Start with an impossibly low score to guarantee move will be updated 
        # when we get a worst case score of -1.
        score = -2

        # Loop through the 9 indices of the board, goes from 0-8
        for i in range(9):
            # Check if index is empty if it contains "_".
            if currBoard[i] == "_":
                # Make a copy of the board to run tests on.
                nextMoveBoard = currBoard.copy()
                # Set index we are testing to letter of the current player. O or X
                nextMoveBoard[i] = player
                # Make a recursive call to minimax() to find all possible 
                # outcomes of the move we are testing.  Find the opponent 
                # of the current player and pass them into the recursive call.
                # This will cause the player to switch between AI and User at 
                # each level of recursion. Minimax will return the best score
                # possible from all potential outcomes of this move and the 
                # calculated best move
                scoreForMove, returnedMove = self.minimax(nextMoveBoard, self.getOpponent(player))
                # If the score returned from the recursive call is better than 
                # the current score, update the score. scoreForMove is negated 
                # here because the score just calculated was for the opponent.
                if (-scoreForMove) > score:
                    # scoreForMove is negated here for the same reason as above
                    score = -scoreForMove
                    # Record the move that led to this new high score
                    bestMove = i

        # If move is never updated, it will still equal -1. This means there
        # are no potential moves left in this scenario so the scenario will 
        # end in a draw.
        if bestMove == -1:
            # We return zero here so the score is neither increased nor 
            # decreased for this scenario.
            return 0, bestMove

        # Each recursive call will return score and bestMove
        return score, bestMove


    # This method returns the opponent of the player that is passed in
    def getOpponent(self, player):
        if player == "O":
            return "X"
        elif player == "X":
            return "O"


    # This method overrides the standard save method to check for a winner 
    # and call for an AI move if necessary.
    def save(self, *args, **kwargs):
        # Check if a response has been requested by a new user move.
        if self.response: 
            winner = self.checkWinner(list(self.board))
            # Check if the user won with their latest move.
            if winner == "X":
                # If the user did win, set winner to X
                self.winner = "X"
            else:
                # If user did not win, generate a new AI move.
                self.AIMove()

        return super(Game, self).save(*args, **kwargs)


    # This method checks if the user or AI has won the game.  The method will
    # return 0 if there is no winner, return O if the AI has won, and return 
    # X if the user has won.
    def checkWinner(self, board):
        for scenario in self.WINSCENARIOS:
            contents = (board[scenario[0]],board[scenario[1]],board[scenario[2]])
            if contents == ("X", "X", "X"):
                return "X"
            if contents == ("O", "O", "O"):
                return "O"
        return "0"

    # This is a list of all the possible winning scenarios.
    WINSCENARIOS = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left Column
        [1, 4, 7],  # Middle Column
        [2, 5, 8],  # Right Column
        [0, 4, 8],  # Top Left to bottom right diagonal
        [2, 4, 6],  # Top right to bottom left diagonal
    ]
