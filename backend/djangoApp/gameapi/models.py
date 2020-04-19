from django.db import models

# This model holds information about the current game.  The board is a string 
# with a length of 9, allowing 1 letter for each of the 9 spaces on the board.
# Currently the board is 9 empty spaces but will be filled later

class Game(models.Model):
    board = models.CharField(max_length=9, default=" " * 9)

    # This specifies what to print when this model is printed
    def __str__(self):
        self.AIMove()
        return self.board # Prints contents of board field

    def AIMove(self):
        listConv = list(self.board)
        listConv[3] = "O" 
        self.board = "".join(listConv)
