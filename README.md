# Tic Tac Toe

This game of tic tac toe is composed of a Vue.js frontend and a Django backend 
that are completely separated.  The frontend and backend communicate via API 
only. Both the Node server and the Django server must be running for the app to 
work properly.

# Javascript Single Page Application

The Vue.js frontend displays the contents of the game board, accepts user 
input, and makes API requests when the player makes a new move or the game 
resets. The Vue app runs on a node.js server.

npm will be used to install dependencies.

### Install dependencies
```
cd spa
npm install
```

### Start development server
```
npm run serve
```

### Access Single Page Application

Once the node server is running, navigate to the "Local" address visible in the
terminal window in a web browser.  Testing was done with Chrome.  Results may vary with other browsers.


# Django Backend

The Django backend consists of a SQLite database and an API. The backend handles all
game logic and calculates moves for the unbeatable AI opponent.

This app requires Python 3.7.7 to run.  It is recommended to use a python 
virtual environment for dependencies. Pip is used to install dependencies.

### Install Django dependencies
```
cd backend
pip install -r requirements.txt
```

### Start development server
```
python manage.py runserver
```

### Opponent AI

The AI cannot be beat without exploiting bugs in the frontend application.  The best a user can do is tie the game against the AI.  The algorithm used to create the opponent AI is called the minimax algorithm.  More can be read about this algorithm and its uses in AI [here] (https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1).

### API Usage

A POST request from the frontend prompts the creation of a new game object in 
the database. When a player makes a new move, the frontend sends a PUT request
to update the game object.  The backend receives the new move and computes a 
new AI move in response to the user move.  The move is then sent back to the
frontend in the PUT request response.

# Known Errors

- Users can choose squares already occupied by the AI's characters as their next move.  This will allow the player to rewrite history and win.
- There is currently nothing to handle games that end in a draw.  User's must reload the page to start a new game.
- My own testing has shown the AI to be very capable.  Please contact me if you are able to beat it. I would love to see how you did it.