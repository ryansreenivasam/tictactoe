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
        return self.board # Prints contents of board field


    # This method will hold the logic for the AI opponent
    def AIMove(self):
        boardList = list(self.board) # split board string into list

        boardList[3] = "O" # placeholder to show that we went through this

        self.board = "".join(boardList) # join boardList back into string

        #TODO check if this AI move has won the game

    # This method overrides the standard save method to check for a winner 
    # and call for an AI move if necessary.
    def save(self, *args, **kwargs):
        if self.response: # Check if a response has been requested
            if self.winner == "0": # Check if the user won with their last move
                self.AIMove() # If user did not win, get a new AI move

        return super(Game, self).save(*args, **kwargs)


    # This method checks if the user or AI has won the game.  The method will
    # return 0 if there is no winner, return O if the AI has won, and return 
    # X if the user has won.
    # The property tag will make this act like a field.
    @property
    def winner(self):
        # TODO Add logic to identify if someone has won
        
        # TODO set response to false if someone has won
       
        return "0"
