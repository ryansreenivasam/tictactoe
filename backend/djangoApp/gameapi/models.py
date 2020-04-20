from django.db import models

# This model holds information about the current game.  The board is a string 
# with a length of 9, allowing 1 letter for each of the 9 spaces on the board.
# The board begins as a string with 9 blank spaces.  The active field determines
# if the board is currently being used in a game.  When a game starts, this
# field is set to active allowing the AI to make moves in response to the user.
# When a winner is declared, active is set to false to prevent alterations to
# the data while the game remains in the database.

class Game(models.Model):
    board = models.CharField(max_length=9, default=" " * 9)
    active = models.BooleanField(default=False)

    # This specifies what to print when this model is printed
    def __str__(self):
        return self.board # Prints contents of board field

    # This method will hold the logic for the AI opponent
    def AIMove(self):
        boardList = list(self.board) # split board string into list

        boardList[3] = "O" # placeholder to show that we went through this

        self.board = "".join(boardList) # join boardList back into string

    # This method overrides the standard save method to check for a winner 
    # and call for an AI move if necessary.
    def save(self, *args, **kwargs):
        if self.active: # Check if game is currently in use
            if not self.winner(): # Check if the user won with their last move
                self.AIMove() # If user did not win, get a new AI move
                
        return super(Game, self).save(*args, **kwargs)


    # This method checks if the user or AI has won the game.  The method will
    # return True if there is a winner and false if there is not.
    def winner(self):
        # TODO Add logic to identify if someone has won
        winner = False 

        # TODO set winner to true and active to false if someone has won
       
        return winner
