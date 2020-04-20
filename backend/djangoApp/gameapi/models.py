from django.db import models

# This model holds information about the current game.  The board is a string 
# with a length of 9, allowing 1 letter for each of the 9 spaces on the board.
# The board begins as a string with 9 blank spaces.  The response field determines
# if an AI move has been requested. Response will be set to True after a new user 
# move has been received.

class Game(models.Model):
    board = models.CharField(max_length=9, default=" " * 9)
    response = models.BooleanField(default=False)

    # This specifies what to print when this model is printed
    def __str__(self):
        # Prints contents of board field
        return self.board


    # This method converts the board string into a list then passes that list 
    # to the minimax function to calculate the next move.
    def AIMove(self):
        # Split board string into list for further manipulation.
        boardList = list(self.board) 
        print(boardList)
         # Pass current board and A for AI player to find the next AI move.
        score = self.minimax(boardList, "A")
        print(score)

        # Join indices of boardList into string and assign to board field.
        self.board = "".join(boardList)
        print(self.board)

        #TODO check if this AI move has won the game


    # This method will determine the next move that the AI will make.  The
    # move is determined by using the minimax algorithm to recursively look 
    # through all possible future moves and choose the move that will win.
    # currBoard is the relevant board in list form.  player is the current 
    # player that is taking a turn.  player will either be "A" for AI or "U"
    # for user.  When minimax() is first called by AIMove, "A" is passed in 
    # so that a move for the AI is produced at the end of the process.

    def minimax(self, currBoard, player):
        if self.winner == player: # TODO need to update winner method for this to work
            # If the current player has won the game, return 1 to indicate that
            # this scenario is favorable to the current player.
            return 1 

        # Start with a move that is not possible.
        move = -1
        # Start with an impossibly low score to guarantee move will be updated 
        # when we get a worst case score of -1.
        score = -2

        # Loop through the 9 indices of the board, goes from 0-8
        for i in range(9):
            # Check if index is empty if it contains "_".
            if currBoard[i] == "_":
                # Make a copy of the board to run tests on.
                nextMoveBoard = currBoard.copy()
                # Set index we are testing to letter of the current player. A or U
                nextMoveBoard[i] = player
                print(nextMoveBoard, " nextMoveBoard")
                # Make a recursive call to minimax() to find all possible 
                # outcomes of the move we are testing.  Find the opponent 
                # of the current player and pass them into the recursive call.
                # This will cause the player to switch between AI and User at 
                # each level of recursion. Minimax will return the best score
                # possible from all potential outcomes of this move.
                scoreForMove = -self.minimax(nextMoveBoard, self.getOpponent(player))
                # If the score returned from the recursive call is better than 
                # the current score, update the score. 
                if scoreForMove > score:
                    score = scoreForMove
                    # Record the move that led to this new high score
                    move = i

        # If move is never updated, it will still equal -1. This means there
        # are no potential moves left in this scenario so the scenario will 
        # end in a draw.
        if move == -1:
            # We return zero here so the score is neither increased nor 
            # decreased for this scenario.
            print("this game will be a draw")
            return 0

        # Each recursive call will return score.
        return score


    # This method returns the opponent of the player that is passed in
    def getOpponent(self, player):
        if player == "A":
            return "U"
        elif player == "U":
            return "A"


    # This method overrides the standard save method to check for a winner 
    # and call for an AI move if necessary.
    def save(self, *args, **kwargs):
        # Check if a response has been requested by a new user move.
        if self.response: 
            # Check if the user won with their latest move.
            if self.winner == "0":
                # If user did not win, generate a new AI move.
                self.AIMove()

        return super(Game, self).save(*args, **kwargs)


    # This method checks if the user or AI has won the game.  The method will
    # return 0 if there is no winner, return A if the AI has won, and return 
    # U if the user has won.
    # The property tag will make this act like a field.
    @property
    def winner(self):
        # TODO Add logic to identify if someone has won
        
        # TODO set response to false if someone has won
       
        return "0"
